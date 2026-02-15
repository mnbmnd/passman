# Passman TODO
**Author**: Muneeb Mennad\
**Project Name**: Passman\
**File Name**: TODO.md\
**Project Start**: 2026-01-24\
**Github Profile**: https://github.com/mnbmnd/
___
## Current
- [x] Add `has_master_credentials()` function to `authentication.py`
  - Check if `master.json` exists
  - Check if file is not empty
  - Validate JSON structure (username, salt, hash)
  - Return `True` if valid, `False` otherwise

- [ ] Update `credentials_menu()` in `main.py`
  - Call `has_master_credentials()` at start
  - If `False`: Show Menu1 (Setup / Quit)
  - If `True`: Show Menu2 (Login / Settings / Quit)

- [ ] Test both scenarios
  - Test with no `master.json` → should show Setup
  - Test with valid `master.json` → should show Login
  - Test with empty/invalid `master.json` → should show Setup

- [ ] Fix functions and file structure
  - Move menus to their file
  - Move authentication and setups to their file

## Hand-off
- [ ] Update README.md

## Later
- [ ] Add Settings menu for updating master password
  - Require login first
  - Verify old password before allowing update
  
- [ ] Implement password vault storage (`passwords.json`)
  - Encrypt vault with key derived from master password
  - Add check for vault file to prevent credential overwrites

- [ ] Add fuzzy matching for `passman <site>` CLI
  - Install `rapidfuzz`
  - Implement site name matching

- [ ] Add clipboard support
  - Install `pyperclip`
  - Auto-copy passwords on retrieval

- [ ] Add TUI (when going full scale)
  - Consider `prompt_toolkit` or `textual`
  - Add Enter/ESC navigation

## Completed ✓
- [x] Master password authentication with PBKDF2
- [x] Password generation (passphrase + alphanumeric)
- [x] Entropy/strength checker
- [x] Menu system

###### END_FILE  
