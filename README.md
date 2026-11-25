# ai-media-cost-guard

[![CI](https://github.com/tarikra1/ai-media-cost-guard/actions/workflows/ci.yml/badge.svg)](https://github.com/tarikra1/ai-media-cost-guard/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/release-v1.0.0-0EA5E9.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Pre-flight credit & USD cost simulator and budget gate for autonomous AI media agents (image, video, TTS, and 3D generation).**

Prevents accidental credit burn by calculating exact credit deductions, effective annual/monthly USD equivalents, and projected remaining balance before any paid API tool runs.

## Quickstart

```bash
pip install -e .
cost-guard video_5s_1080p --units 3 --balance 12500 --max-usd 1.50
```

## License

MIT License — see [LICENSE](LICENSE).
