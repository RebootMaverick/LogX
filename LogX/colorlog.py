import datetime

def infolog(message, path=None):
    if path is not None:
        with open(path, 'a') as file:
            file.write(message + '\n')
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log_message = f"\033[2;97m{current_time} \033[0m\033[34mINFO \033[0m{message}"
            return log_message
    else:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"\033[2;97m{current_time} \033[0m\033[34mINFO \033[0m{message}"
        return log_message
    
def errorlog(message,path=None):
    if path is not None:
        with open(path, 'a') as file:
            file.write(message + '\n')
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log_message = f"\033[2;97m{current_time} \033[0m\033[31mERROR \033[0m{message}"
            return log_message
    else:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"\033[2;97m{current_time} \033[0m\033[31mERROR \033[0m{message}"
        return log_message
    
def debuglog(message,path=None):
    if path is not None:
        with open(path, 'a') as file:
            file.write(message + '\n')
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log_message = f"\033[2;97m{current_time} \033[0m\033[33mDEBUG \033[0m{message}"
            return log_message
    else:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"\033[2;97m{current_time} \033[0m\033[33mDEBUG \033[0m{message}"
        return log_message

def criticallog(message,path=None):
    if path is not None:
        with open(path, 'a') as file:
            file.write(message + '\n')
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log_message = f"\033[2;97m{current_time} \033[0m\033[35mCRITICAL \033[0m{message}"
            return log_message
    else:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"\033[2;97m{current_time} \033[0m\033[35mCRITICAL \033[0m{message}"
        return log_message

def warninglog(message,path=None):
    if path is not None:
        with open(path, 'a') as file:
            file.write(message + '\n')
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log_message = f"\033[2;97m{current_time} \033[0m\033[90mWARNING \033[0m{message}"
            return log_message
    else:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"\033[2;97m{current_time} \033[0m\033[90mWARNING \033[0m{message}"
        return log_message

print(debuglog('hello','log.text'))