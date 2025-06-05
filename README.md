# 📝 Blog Post Generator

A simple Flask-based application that generates SEO-friendly blog posts based on a keyword.

---

## ⚙️ Prerequisites

Ensure you have **Python** installed on your system.  
You can verify this by running:

```bash
python --version
```

---

## 📥 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

Make sure you are in the project directory, then start the app with:

```bash
python app.py
```

Once running, open your browser and go to:  
**http://127.0.0.1:5000**
This ensures the application is running

---

## 🧠 Generating a Blog Post

To generate a blog post based on a keyword, use the following URL format in your browser:

```
http://127.0.0.1:5000/generate?keyword=your-keyword
```

**Example:**

```
http://127.0.0.1:5000/generate?keyword=monitor
```

---

## ⏰ Scheduling Daily Generation

To configure the frequency of automatic blog generation:

- Open `scheduler.py`
- Go to **line 22**
- Modify the scheduling interval

**Default:**  
```python
scheduler.add_job(routine, 'interval', minutes=1)
```
- Saved scheduler blogs are saved in the generated folder

Change this to your desired frequency.



