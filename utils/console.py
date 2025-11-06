from colorama import init, Fore, Style

# Para iniciar colorama
init(autoreset=True)

def info(msg):
    return Fore.CYAN + "ℹ️  " + msg

def success(msg):
    return Fore.GREEN + "✅ " + msg

def warn(msg):
    return Fore.YELLOW + "⚠️  " + msg

def error(msg):
    return Fore.RED + "❌ " + msg

def title(msg):
    return Style.BRIGHT + msg

