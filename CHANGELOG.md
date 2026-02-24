# Changelog

All notable changes to this project will be documented in this file.

## [2026-02-24] - Comprehensive 2026 Audit & Cleanup

### Added
- **Anthropic Specific Models:**
  - `prompts/Anthropic/Claude 4.5 Sonnet.txt`
  - `prompts/Anthropic/Claude 4.6 Sonnet.txt`
  - `prompts/Anthropic/Claude 4.6 Opus.txt`
- **Google Specific Models:**
  - `prompts/Google/Gemini 1.5 Pro.txt`
  - `prompts/Google/Gemini 1.5 Flash.txt`
- **OpenAI / ChatGPT Specific Models:**
  - `prompts/OpenAI/o3-mini.txt`
  - `prompts/OpenAI/GPT-4.5.txt`
- **Perplexity Specific Models:**
  - `prompts/Perplexity/Sonar Reasoning.txt`
- Code snippets and explicit execution settings (Temperature, Top-p) across all prompt text files.
- `verify-prompts.py` to enforce a zero-placeholder policy across the codebase in CI.

### Changed
Removed the exact placeholder: *"This prompt is currently undergoing our rigorous 9/10 quality assurance process. Check back later or submit a PR!"* from the following files and replaced them with fully detailed, runnable 2026 master prompts:
- `prompts/Amp/Prompt.txt`
- `prompts/Anthropic/Prompt.txt`
- `prompts/Augment Code/Prompt.txt`
- `prompts/Cluely/Prompt.txt`
- `prompts/CodeBuddy Prompts/Prompt.txt`
- `prompts/Comet Assistant/Prompt.txt`
- `prompts/Dia/Prompt.txt`
- `prompts/Google/Prompt.txt`
- `prompts/Kiro/Prompt.txt`
- `prompts/Leap.new/Prompt.txt`
- `prompts/Lovable/Prompt.txt`
- `prompts/Open Source prompts/Prompt.txt`
- `prompts/Orchids.app/Prompt.txt`
- `prompts/Poke/Prompt.txt`
- `prompts/Traycer AI/Prompt.txt`
- `prompts/v0 Prompts and Tools/Prompt.txt`
- `prompts/Xcode/Prompt.txt`

Every prompt is now fully autonomous and deployment-ready.
