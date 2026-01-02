# Known and Likely Issues (Error Log)

This document summarizes issues observed in the codebase during
development and common problems likely encountered.

## Observed Issues

1.  **Hardcoded credentials**
    -   Database credentials were initially hardcoded in
        `conexion_db.py`.
    -   **Impact:** Security risk when pushing to GitHub.
    -   **Fix:** Moved to environment variables using `.env` and
        `python-dotenv`.
2.  **Inconsistent imports / paths**
    -   Imports did not match actual folder structure in `main.py`.
    -   **Impact:** `ModuleNotFoundError`.
    -   **Fix:** Updated imports to align with `src/` layout.
3.  **Use of print instead of logging**
    -   Status and error messages used `print()`.
    -   **Impact:** No persistent error history.
    -   **Fix:** Introduced centralized logging via `config/logger.py`.
4.  **Logger misuse**
    -   Logger calls placed outside `main()` and unconditional `error`
        logs.
    -   **Impact:** Misleading logs.
    -   **Fix:** Scoped logs properly and used correct log levels.
5.  ****pycache** committed**
    -   Python cache folders present.
    -   **Impact:** Repository noise.
    -   **Fix:** Removed and added to `.gitignore`.

## Likely Runtime Issues

1.  **API timeout or connection errors**
    -   External API may fail or respond slowly.
    -   **Mitigation:** Timeouts and exception handling in API provider.
2.  **Empty DataFrame handling**
    -   API may return empty or invalid data.
    -   **Mitigation:** Pipeline stops early if DataFrame is empty.
3.  **PDF font path issues**
    -   Hardcoded Windows font paths.
    -   **Mitigation:** Fallback to default font if not found.
4.  **Database connection failures**
    -   MySQL service down or wrong credentials.
    -   **Mitigation:** Logging errors and safe connection close.
5.  **Excel overwrite conflicts**
    -   File open while writing.
    -   **Mitigation:** Use context manager and replace sheets safely.

## Notes

-   This file is informational and not auto-generated.
-   Intended to document development pitfalls and learning points.

## Bug: generate_kpis fails when the DataFrame does not contain the `count` column

**Status:** Fixed ✅  
**Detected by:** Unit tests (pytest)

### Description
The `generate_kpis` function assumed that the input DataFrame always contained a `count` column.
When the DataFrame did not include this column, the following error occurred:

