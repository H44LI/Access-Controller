# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked = [302, 246, 229, 147]
approved = []
denied = []
while True:
    name = input("What is your name | type 'done' to finish ")
    if name.lower() == 'done':
        break
    else:
        badge_no = int(input("What is your badge number"))
        if badge_no in revoked:
            denied.append(name)
            print("Acess denied - Your badge has been revoked")
        else:
            approved.append(name)
            print("Acess granted")
print('***Acess Summary***')
print("Approved Visitors-")
for person in sorted(approved):
    print(f'>{person}')
print("Denied Visitors-")
for person in sorted(denied):
    print(f'>{person}')

print(f"""Total approved visitors = {len(approved)} 
Total Denied visitors = {len(denied)}""")