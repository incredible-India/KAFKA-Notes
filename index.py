import subprocess
import os

# Ensure the current working directory is set to the cloned repository
repo_path = r"C:\Users\himanshu.y.sharma\\Desktop\\Git pusher\\KAFKA-Notes"

# Open the source file in read mode and the destination file in append mode
with open('./in.txt', 'r') as source, open('./README.md', 'a') as destination:
    # Loop through each line in the source file
    for line in source:
        # Write the line to the destination file
        destination.write(line)

        try:
            # Stage the changes
            subprocess.run(['git', 'add', '--a'], cwd=repo_path, check=True)

            # Check if there are any changes to commit
            result = subprocess.run(
                ['git', 'status', '--porcelain'], cwd=repo_path, capture_output=True, text=True
            )

            if not result.stdout.strip():
                print(f"No changes to commit for line: {line.strip()}")
                #continue

            # Commit the changes with the line content as the commit message
            commit_message = f"Added line: {line.strip()[:50]}"  # Truncate message to 50 characters
            subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path, check=True)

            # Push the changes
            subprocess.run(['git', 'push'], cwd=repo_path, check=True)

            print(f"Processed and pushed: {line.strip().split(' ')[0]}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            break  # Stop processing if
