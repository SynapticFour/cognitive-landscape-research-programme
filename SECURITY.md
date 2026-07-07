# Security Policy

## Scope

The Cognitive Landscape Research Programme (CLRP) repository contains **documentation and minimal maintenance scripts**. It does not operate production services, store participant data, or run assessment instruments.

Security concerns for CLRP fall into two categories:

1. **This repository** — integrity of programme documentation, supply chain of scripts, GitHub account access.
2. **Related implementations** — PCMS, CLM, and deployed instruments (report to those repositories' security policies).

## Supported versions

CLRP releases are tagged (`clrp-v*`). Security-relevant amendments to **Accepted** documents are backported to the current release branch when they correct factual errors that could cause harm (e.g. misstated ethical constraints).

| Release tag | Supported |
|-------------|-----------|
| Latest `clrp-v*` | Yes |
| Older tags | Documentation only; no active patches unless critical |

## Reporting a vulnerability

**Do not open public GitHub issues for security vulnerabilities.**

Email [contact@synapticfour.com](mailto:contact@synapticfour.com) with:

- Description of the issue
- Steps to reproduce (if applicable)
- Affected files, releases, or related repositories
- Your assessment of impact
- Optional: suggested remediation

We aim to acknowledge reports within **5 business days**.

## What belongs here vs elsewhere

| Concern | Report to |
|---------|-----------|
| CLRP repo tampering, malicious script in `scripts/` | This policy |
| PCMS web application vulnerability | [PCMS SECURITY.md](https://github.com/SynapticFour/perceptual-cognitive-mapping-system/blob/main/SECURITY.md) |
| CLM library vulnerability | [CLM SECURITY.md](https://github.com/SynapticFour/cognitive-landscape-model/blob/main/SECURITY.md) |
| Participant data breach in a deployment | Deployment operator + [contact@synapticfour.com](mailto:contact@synapticfour.com) |
| Misuse of programme outputs for gatekeeping or discrimination | [contact@synapticfour.com](mailto:contact@synapticfour.com) (ethics, not CVE) |

## Documentation integrity

Because CLRP documents may inform research ethics and institutional review:

- Changes to **Accepted** normative documents (especially [CLRP-007](clrp/CLRP-007-non-diagnostic-commitment.md)) require version bumps and changelog entries.
- Force-pushes to `main` are prohibited by repository policy.
- Release tags are immutable.

## Scripts

If `scripts/` grows beyond trivial maintenance tooling, each script should:

- Avoid network calls except where explicitly documented
- Not process secrets or participant data
- Pin dependencies if a package manifest is introduced

## Disclosure policy

We follow coordinated disclosure. We will:

1. Confirm the issue
2. Develop a fix or documentation correction
3. Release a patched version or errata
4. Credit reporters who wish to be named

## Safe harbour

We support good-faith security research on publicly deployed Synaptic Four properties within the scope of their stated policies. Research that involves human participants must follow applicable ethics law independently of this policy.
