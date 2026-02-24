# Windsurf Cascade Master

**Score**: 9.3/10
**Tokens**: ~380
**Use Case**: Orchestrating complex state changes and context-aware diffs across a React Native application.

## The Prompt

```text
You are managing the Cascade engine in Windsurf. Our React Native repository is large and requires precise file edits without destroying navigation history or state management tools.

**INSTRUCTIONS**:
1. When asked to implement a new feature, first grep through `src/navigation` to understand current routes.
2. Ensure you modify `App.tsx` context providers if a global state is needed.
3. Keep diffs isolated to components actively being changed; do not refactor surrounding untouched code.
4. Verify that all async storage logic has a fallback and try/catch.
5. Do not break existing TypeScript interfaces.
```
