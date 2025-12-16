# ============================================================
# LOGGING IN PYTHON – COMPLETE NOTES
# ============================================================

# Logging ka use:
# ➜ Software run ke dauran events track karna
# ➜ Debugging
# ➜ Error monitoring
# ➜ Production issues trace karna

import logging


# ============================================================
# LOGGING LEVELS (LOW → HIGH SEVERITY)
# ============================================================

# DEBUG     → Detailed debugging info
# INFO      → Program normal chal raha hai
# WARNING   → Potential issue
# ERROR     → Serious issue, program chalta rahega
# CRITICAL  → Program crash / terminate hone wali situation


# ============================================================
# BASIC LOGGING CONFIGURATION
# ============================================================

logging.basicConfig(
    filename="app.log",           # log file name
    level=logging.DEBUG,           # minimum level to log
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# NOTE:
# Iske baad basicConfig dubara call mat karna


# ============================================================
# LOG MESSAGES
# ============================================================

logging.debug("Debugging started")
logging.info("Application started successfully")
logging.warning("Disk space is running low")
logging.error("File not found")
logging.critical("System crash imminent")


# ============================================================
# WHY DEBUG LOG NAHI DIKHTA KABHI-KABHI?
# ============================================================

# Agar level = INFO
# ➜ DEBUG logs ignore ho jaate hain
#
# Rule:
# "Level ke niche wale hi logs show honge"


# ============================================================
# REAL PROGRAM USAGE (INTERVIEW + PRACTICAL)
# ============================================================

def divide(a, b):
    logging.info("divide() function called")
    try:
        result = a / b
        logging.debug(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        return None


divide(10, 2)
divide(10, 0)


# ============================================================
# LOGGING TO CONSOLE + FILE (ADVANCED)
# ============================================================

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# File Handler
file_handler = logging.FileHandler("advanced.log")
file_handler.setLevel(logging.DEBUG)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Format
formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# ============================================================
# USING LOGGER IN PROGRAM
# ============================================================

def login(user):
    logger.info(f"User {user} attempting login")

    if user != "admin":
        logger.warning("Unauthorized login attempt")
    else:
        logger.info("Login successful")


login("guest")
login("admin")
