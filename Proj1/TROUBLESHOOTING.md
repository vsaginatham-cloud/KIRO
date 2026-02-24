# 🔧 Troubleshooting Guide - TTD Chatbot

## Common Installation Issues

### 1. Python Not Found

**Error:**
```
'python' is not recognized as an internal or external command
```

**Solution:**
- Install Python 3.8+ from https://python.org
- During installation, check "Add Python to PATH"
- Restart your terminal/command prompt
- Verify: `python --version`

---

### 2. pip Not Found

**Error:**
```
'pip' is not recognized as an internal or external command
```

**Solution:**
```bash
# Windows
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Linux/Mac
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

---

### 3. Permission Denied (Linux/Mac)

**Error:**
```
Permission denied
```

**Solution:**
```bash
# Use pip with --user flag
pip3 install -r requirements.txt --user

# Or use sudo (not recommended)
sudo pip3 install -r requirements.txt
```

---

### 4. Module Not Found Errors

**Error:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solution:**
```bash
# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall

# Or install specific module
pip install streamlit
```

---

### 5. googletrans Installation Error

**Error:**
```
ERROR: Could not find a version that satisfies the requirement googletrans==4.0.0rc1
```

**Solution:**
We've replaced googletrans with deep-translator. Update your requirements.txt:
```bash
# Remove old package
pip uninstall googletrans

# Install new package
pip install deep-translator
```

---

## API Key Issues

### 6. GEMINI_API_KEY Not Found

**Error:**
```
ValueError: GEMINI_API_KEY not found. Please set it in .env file
```

**Solution:**
1. Check if `.env` file exists in Proj1 folder
2. Open `.env` and verify it contains:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```
3. Make sure there are no extra spaces or quotes
4. Restart the application

---

### 7. Invalid API Key

**Error:**
```
google.api_core.exceptions.InvalidArgument: Invalid API key
```

**Solution:**
1. Get a new API key from: https://makersuite.google.com/app/apikey
2. Update `.env` file with the new key
3. Make sure you copied the entire key
4. Check for any extra characters or spaces

---

### 8. API Quota Exceeded

**Error:**
```
Resource has been exhausted (e.g. check quota)
```

**Solution:**
- You've exceeded the free tier limit
- Wait for quota to reset (usually daily)
- Or upgrade to paid tier
- Check usage at: https://console.cloud.google.com

---

## Application Runtime Issues

### 9. Port Already in Use

**Error:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**
```bash
# Option 1: Use different port
streamlit run app.py --server.port 8502

# Option 2: Kill existing process (Windows)
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Option 2: Kill existing process (Linux/Mac)
lsof -ti:8501 | xargs kill -9
```

---

### 10. Streamlit Won't Start

**Error:**
```
streamlit: command not found
```

**Solution:**
```bash
# Reinstall streamlit
pip install --upgrade streamlit

# Or run with python -m
python -m streamlit run app.py
```

---

### 11. Translation Not Working

**Error:**
```
Translation error: ...
```

**Solution:**
- Check internet connection
- Verify deep-translator is installed: `pip show deep-translator`
- Try reinstalling: `pip install --upgrade deep-translator`
- Translation requires active internet connection

---

### 12. Language Detection Fails

**Error:**
```
Language detection error: ...
```

**Solution:**
- Check if langdetect is installed: `pip show langdetect`
- Reinstall: `pip install --upgrade langdetect`
- Try typing longer sentences (detection works better with more text)

---

## Import Errors

### 13. Cannot Import from config

**Error:**
```
ImportError: cannot import name 'GEMINI_API_KEY' from 'config'
```

**Solution:**
1. Check if `config.py` exists in Proj1 folder
2. Verify `.env` file exists and has API key
3. Try running from Proj1 directory:
   ```bash
   cd Proj1
   streamlit run app.py
   ```

---

### 14. Cannot Import from utils

**Error:**
```
ModuleNotFoundError: No module named 'utils'
```

**Solution:**
1. Check if `utils/` folder exists
2. Check if `utils/__init__.py` exists
3. Run from correct directory (Proj1 folder)
4. Try:
   ```bash
   export PYTHONPATH="${PYTHONPATH}:."  # Linux/Mac
   set PYTHONPATH=%PYTHONPATH%;.        # Windows
   ```

---

### 15. Cannot Import from data

**Error:**
```
ModuleNotFoundError: No module named 'data'
```

**Solution:**
1. Check if `data/` folder exists
2. Check if `data/__init__.py` exists
3. Verify you're in the Proj1 directory
4. Check file structure matches documentation

---

## UI/Display Issues

### 16. Blank Page or White Screen

**Solution:**
1. Clear browser cache
2. Try different browser
3. Clear streamlit cache:
   ```bash
   streamlit cache clear
   ```
4. Check browser console for errors (F12)

---

### 17. Sidebar Not Showing

**Solution:**
1. Click the arrow (>) on the left side to expand sidebar
2. Check browser width (sidebar auto-hides on narrow screens)
3. Try refreshing the page (Ctrl+R or Cmd+R)

---

### 18. CSS Not Loading

**Solution:**
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Clear browser cache
3. Check if custom CSS in app.py is correct

---

## Data/Content Issues

### 19. Booking Dates Not Showing

**Solution:**
1. Check if `data/booking_calendar.py` exists
2. Verify imports in app.py
3. Check browser console for JavaScript errors
4. Try restarting the application

---

### 20. Seva Information Missing

**Solution:**
1. Check if `data/ttd_knowledge_base.py` exists
2. Verify the file has correct Python syntax
3. Check imports in `utils/gemini_chat.py`
4. Restart the application

---

## Performance Issues

### 21. Slow Response Times

**Solution:**
- Check internet connection speed
- Gemini API calls require internet
- Try during off-peak hours
- Consider upgrading to paid API tier for faster responses

---

### 22. Application Crashes

**Solution:**
1. Check error message in terminal
2. Verify all dependencies are installed
3. Check system resources (RAM, CPU)
4. Try running test script:
   ```bash
   python test_installation.py
   ```

---

## Testing & Debugging

### 23. Run Installation Test

To diagnose issues, run the test script:

```bash
python test_installation.py
```

This will check:
- ✓ All required imports
- ✓ Project file structure
- ✓ Environment configuration
- ✓ Module imports

---

### 24. Enable Debug Mode

Add to your `.env` file:
```
DEBUG=True
```

Or run streamlit with debug flag:
```bash
streamlit run app.py --logger.level=debug
```

---

### 25. Check Logs

Streamlit logs are usually in:
- Windows: `%USERPROFILE%\.streamlit\logs\`
- Linux/Mac: `~/.streamlit/logs/`

---

## Environment Issues

### 26. Wrong Python Version

**Check version:**
```bash
python --version
```

**Solution:**
- Install Python 3.8 or higher
- Use virtual environment:
  ```bash
  python -m venv venv
  
  # Activate (Windows)
  venv\Scripts\activate
  
  # Activate (Linux/Mac)
  source venv/bin/activate
  
  # Install dependencies
  pip install -r requirements.txt
  ```

---

### 27. Multiple Python Installations

**Solution:**
Use specific Python version:
```bash
# Windows
py -3.9 -m pip install -r requirements.txt
py -3.9 -m streamlit run app.py

# Linux/Mac
python3.9 -m pip install -r requirements.txt
python3.9 -m streamlit run app.py
```

---

### 28. Virtual Environment Issues

**Solution:**
```bash
# Deactivate current environment
deactivate

# Remove old environment
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows

# Create fresh environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Reinstall
pip install -r requirements.txt
```

---

## Network Issues

### 29. Firewall Blocking

**Solution:**
- Allow Python through firewall
- Allow Streamlit through firewall
- Check corporate proxy settings
- Try different network

---

### 30. Proxy Configuration

**Solution:**
Set proxy in environment:
```bash
# Windows
set HTTP_PROXY=http://proxy:port
set HTTPS_PROXY=http://proxy:port

# Linux/Mac
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port
```

---

## Still Having Issues?

### Quick Diagnostic Steps:

1. **Run test script:**
   ```bash
   python test_installation.py
   ```

2. **Check Python version:**
   ```bash
   python --version
   ```

3. **Verify dependencies:**
   ```bash
   pip list
   ```

4. **Check file structure:**
   ```bash
   dir  # Windows
   ls -la  # Linux/Mac
   ```

5. **Try fresh install:**
   ```bash
   pip uninstall -r requirements.txt -y
   pip install -r requirements.txt
   ```

---

### Get Help:

**For TTD Information:**
- Phone: 0877-2277777, 0877-2233333
- Email: complaints@tirumala.org

**For Technical Issues:**
- Review README.md
- Check SETUP_GUIDE.md
- Run test_installation.py

---

## Prevention Tips

1. **Always use virtual environment**
2. **Keep dependencies updated**
3. **Never commit .env file**
4. **Backup your API key**
5. **Test after each change**
6. **Read error messages carefully**
7. **Check documentation first**

---

**Om Namo Venkatesaya** 🙏
