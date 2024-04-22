from datetime import datetime

def save_markdown(task_output):
    print("Saving the markdown...")
    current_time = datetime.now()

    filename = f"""{current_time.strftime("%Y-%m-%d-%H:%M:%S")}.md"""

    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result)
    print(f"Markdown saved as {filename}")