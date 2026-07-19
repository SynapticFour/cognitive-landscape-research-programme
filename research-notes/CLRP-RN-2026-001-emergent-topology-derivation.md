---
note-id: CLRP-RN-2026-001
title: Emergent topology derivation (CLM design)
date: 2026-07-20
authors:
  - Synaptic Four
license: CC-BY-4.0
status: Exploratory
clrp-references:
  - CLRP-010
---

# Design note: emergent topology derivation

Companion implementation design for [CLRP-010](../clrp/CLRP-010-structural-theory-geology-of-the-landscape.md) §2.  
Target: `@clm/dynamics`, new module `emergent-topology.ts`, importing `@clm/structural`.

**Date:** 2026-07-20  
**Status:** Exploratory — not normative programme text

## Problem

`AttractorState` (in `attractor.ts`) is currently authored by hand: someone declares a
centroid and radius. `StructuralModel` (in `@clm/structural`) already encodes the latent
parameters and probabilistic influence fields that should, in principle, *produce* a
landscape's attractors — but nothing currently derives one from the other. CLRP-010 G1
requires that this derivation exist before any topology claim can be called "emergent."

## Proposed interfaces

```typescript
// packages/dynamics/src/emergent-topology.ts

import type { StructuralModel } from '@clm/structural';
import type { FeedbackGraph } from './feedback-graph.js';
import type { AttractorState } from './attractor.js';
import type { RandomSource } from '@clm/structural';

export interface TopologySamplingConfig {
  readonly structuralModel: StructuralModel;
  readonly feedbackGraph: FeedbackGraph;
  readonly dimensionIds: readonly string[];
  /** Number of independent latent-parameter draws to simulate. */
  readonly sampleCount: number;
  /** Initial observed-state seeds to relax forward under the dynamics, per sample. */
  readonly seedStates: readonly Readonly<Record<string, number>>[];
  readonly convergenceSteps: number;
  readonly convergenceTolerance: number;
  /** Max distance between two converged points for them to count as the same attractor. */
  readonly clusterRadius: number;
  readonly random?: RandomSource;
}

export interface EmergentAttractor extends AttractorState {
  /** Fraction of (sample x seed) relaxations that converged into this cluster. */
  readonly basinSupport: number;
  /** Range of latent-parameter draws associated with samples converging here — for interpretability, not causal attribution to a single parameter. */
  readonly structuralParameterRanges: Readonly<Record<string, { min: number; max: number }>>;
}

export interface EmergentTopology {
  readonly attractors: readonly EmergentAttractor[];
  /** Fraction of relaxations that did not converge or did not join any sufficiently supported cluster. */
  readonly unclassifiedFraction: number;
  readonly sampleCount: number;
}

export function deriveEmergentTopology(config: TopologySamplingConfig): EmergentTopology;
```

## Algorithm sketch

1. For `sampleCount` iterations: draw a latent-parameter vector from
   `structuralModel`'s priors (or posteriors, if calibrated), propagate through the
   influence fields to obtain a per-dimension bias.
2. For each `seedState`: relax forward under `feedbackGraph`'s dynamics, modulated by
   the sampled structural bias (reusing `structural-modulation.ts`'s
   `applySampleAsModifier`), for up to `convergenceSteps`, stopping early if the
   step-to-step change is below `convergenceTolerance`.
3. Collect all converged end-states (across all samples x seeds).
4. Cluster end-states greedily by Euclidean distance (reuse/export the distance helper
   already private in `attractor.ts`) using `clusterRadius`; each cluster with support
   above a minimum threshold becomes an `EmergentAttractor`, with `basinSupport` =
   cluster size / total relaxations, and `structuralParameterRanges` computed from the
   latent-parameter draws of the samples that landed in that cluster.
5. Relaxations that never converge, or converge into clusters below the support
   threshold, contribute to `unclassifiedFraction`.

## Determinism and testability

- `random` is injectable (matches existing `createSeededRandom` pattern in
  `@clm/structural`), so tests can assert exact clusters for a fixed seed.
- Pure function, no side effects, matches the existing package's style
  (`StructuralModel.define`, `validateAttractor`, etc.).
- Suggested first test fixture: `presets/pcms-parameter-set.ts` (already exists) — derive
  its topology and assert it produces a stable, non-trivial cluster count as a smoke
  test, before any real calibration is attempted.

## Explicitly out of scope for this module

- No claim about which attractor is desirable (CLRP-010 G7) — this module has no
  concept of "good" attractor, only "supported by more/fewer relaxations."
- No fitting to real observational data yet — sampling is from design-informed priors
  only, consistent with CLRP-001 §4 method 3 (computational modelling, not observation)
  until Topology-layer empirical work begins.
- No intervention modelling (changing feedback edges to move a trajectory between
  attractors) — that is explicitly deferred to future CLRP-011-aligned work, once its
  mechanistic/normative separation is established.
