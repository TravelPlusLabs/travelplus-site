# Security Policy

## Scope

This repository contains the static website published at
[usetravelplus.com](https://usetravelplus.com) — HTML and CSS only, with no
server-side code, no build pipeline, and no third-party dependencies.

In scope:

- The published site and its hosting/DNS configuration (for example: domain
  takeover risks, misconfigured HTTPS, content injection).
- Reports about the TravelPlus mobile app are also welcome at the address
  below, even though its source is not in this repository.

Out of scope:

- Findings from automated scanners with no demonstrated impact.
- Missing hardening headers that GitHub Pages does not allow us to set.
- Denial of service, social engineering, and physical attacks.

## Reporting a Vulnerability

Email **contact@usetravelplus.com** with the subject line `SECURITY`.

Please include what you found, the steps to reproduce it, and the impact you
believe it has. If you have a proof of concept, include it.

Please do **not** open a public GitHub issue for a security report.

What to expect:

- We acknowledge reports within **15 business days**.
- We follow up with an assessment — accepted, or declined with the reasoning —
  within **45 business days** of acknowledgement.
- Accepted issues are fixed and deployed as quickly as the severity warrants.
- We are happy to credit you in the fix commit if you would like to be named.

We are a small team and do not run a paid bug bounty program, but we appreciate
reports made in good faith and will not pursue action against researchers who
follow this policy.

## Supported Versions

The site is not versioned. Only the currently deployed content on the `main`
branch is supported and receives fixes.
