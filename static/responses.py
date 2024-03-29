help_response = '''
CALENDAR COMMANDS
!calendar - see the calendar for current month
!today - get today's date
!month month - show calendar of the month

ASSIGNMENTS COMMAND
!save month/day 'assignment' (ex. !save 09/27 'midterm')
!assignments - display lists of assignments due 
!delete #entry - remove assignment from calendar

CHECKLIST COMMANDS
!add 'task' - add tasks to a checklist  (ex. !add 'Do math homework')
!finish #entry - crosses off checklist (ex. !finish #3)
!remove #entry - remove entry from checklist
!clear - remove all entries from checklist
!checklist - displays checklist
                                   
NOTE COMMANDS
!upload [file] - upload a file to be saved (.txt file), replaces existing file if it already exists
!notes - view all uploaded files
!view #entry - send the notes into the chat as a message
!pull #entry - get download link to the selected file
!delete #entry - remove the selected file from storage
                                   
COURSE MANAGEMENT COMMANDS
!schedule [file] - Upload/update your course schedule
!courses - Show your schedule, if a schedule exists
!drop - delete schedule image from storage

POMODORO (TIMER) COMMANDS
!timer #time - start a timer based on the entered number in minutes, defaults to 25 minutes
!restart - restarts the timer back to the original duration
!pause - pauses the timer
'''