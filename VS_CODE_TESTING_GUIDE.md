# Running Tests in Visual Studio Code

This guide helps you run your YouTube tests directly in VS Code.

## 🔧 Setup Complete

Your project is now configured with:
- ✅ Python interpreter pointing to your virtual environment
- ✅ Pytest test discovery enabled  
- ✅ Debug configurations ready
- ✅ Task runners for common test operations

## 🚀 How to Run Tests in VS Code

### Method 1: Using the Testing Panel
1. **Open Testing Panel**: Click the test tube icon in the sidebar (or press `Ctrl+Shift+T`)
2. **Discover Tests**: Click "Refresh Tests" or save any test file
3. **Run Tests**: Click the play button next to any test or test file
4. **View Results**: See results directly in the Testing panel

### Method 2: Using Tasks (Recommended)
1. **Open Command Palette**: `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. **Run Task**: Type "Tasks: Run Task" and select it
3. **Choose Task**:
   - `Run All YouTube Tests` - Runs all tests
   - `Run Single YouTube Test` - Runs only test_youtube.py
   - `Run Smoke Tests` - Runs tests marked with @pytest.mark.smoke
   - `Run YouTube Tests with Allure` - Runs tests with Allure reporting

### Method 3: Using Debug Configuration
1. **Open Run and Debug**: `Cmd+Shift+D` (macOS) or `Ctrl+Shift+D` (Windows/Linux)
2. **Select Configuration**:
   - `Python: Run YouTube Test` - Debug YouTube tests
   - `Python: Run All Tests` - Debug all tests
   - `Python: Debug Single Test` - Debug currently open test file
3. **Start Debugging**: Press F5 or click the green play button

### Method 4: Terminal Integration
1. **Open Integrated Terminal**: `Ctrl+\`` (backtick)
2. **Run Commands**:
   ```bash
   # Run all tests
   .venv/bin/pytest tests/ -v
   
   # Run YouTube tests only
   .venv/bin/pytest tests/test_youtube.py -v
   
   # Run with markers
   .venv/bin/pytest -m smoke -v
   ```

## 📊 Test Results

- **Pass/Fail Status**: Green ✅ or Red ❌ indicators
- **Test Output**: Detailed output in Terminal or Output panel
- **Debugging**: Set breakpoints and step through code
- **Coverage**: Install `pytest-cov` for coverage reports

## 🔍 Quick Tips

1. **Auto-discover**: Tests auto-discover when you save files
2. **Run Individual Tests**: Right-click on a test method → "Run Test"
3. **Keyboard Shortcuts**: 
   - `Ctrl+;` then `Ctrl+A` - Run all tests
   - `Ctrl+;` then `Ctrl+F` - Run failed tests
   - `Ctrl+;` then `Ctrl+L` - Run last test
4. **View Test Output**: Click on test results to see detailed output

## 🐛 Debugging Tests

1. **Set Breakpoints**: Click in the gutter next to line numbers
2. **Debug Test**: Right-click test → "Debug Test" or use F5
3. **Step Through**: Use F10 (step over), F11 (step into), F12 (step out)
4. **Inspect Variables**: Hover over variables or use the Variables panel

## 📁 Files Created for VS Code

- `.vscode/settings.json` - Python and testing configuration
- `.vscode/tasks.json` - Pre-configured tasks for running tests
- `.vscode/launch.json` - Debug configurations
- `.vscode/extensions.json` - Recommended extensions

Your YouTube test automation is now fully integrated with VS Code! 🎉
