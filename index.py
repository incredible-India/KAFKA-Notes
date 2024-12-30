import subprocess

# Ensure the current working directory is set to the cloned repository
repo_path = r"C:\Users\himanshu.y.sharma\Desktop\Git pusher\KAFKA-Notes"

# Open the source file in read mode and the destination file in append mode
with open('./in.txt', 'r') as source, open('./README.md', 'a') as destination:
    # Loop through each line in the source file
    for line in source:
        # Write the line to the destination file
        destination.write(line)
        subprocess.run(['git', 'add', '.'], cwd=repo_path, check=True)

        try:
            # Stage the changes
            

            # Commit the changes with the line content as the commit message
            commit_message = f"Added line: {line.strip()}"
            subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path, check=True)

            # Push the changes
            subprocess.run(['git', 'push'], cwd=repo_path, check=True)

            print(f"Processed and pushed: {line.split(" ")[0]}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            break  # Stop processing if there's an error
