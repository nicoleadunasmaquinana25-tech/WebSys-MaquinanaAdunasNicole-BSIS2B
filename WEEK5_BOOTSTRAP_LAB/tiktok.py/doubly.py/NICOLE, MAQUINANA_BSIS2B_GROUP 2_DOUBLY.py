class Node:

    def __init__(self, video_id, username, caption):
        self.video_id = video_id
        self.username = username
        self.caption = caption

        # Doubly Linked List pointers
        self.prev = None
        self.next = None


def traverse(head):
    if head is None:
        print("\nThe TikTok list is empty.")
        return

    current = head

    print("\n--- TikTok Videos ---")

    while current:
        print(
            f"[ID: {current.video_id} | "
            f"User: @{current.username} | "
            f"Caption: {current.caption}]",
            end=" <-> "
        )

        current = current.next

    print("None")


def traverse_backward(tail):
    if tail is None:
        print("\nThe TikTok list is empty.")
        return

    current = tail

    print("\n--- TikTok Videos (Backward) ---")

    while current:
        print(
            f"[ID: {current.video_id} | "
            f"User: @{current.username} | "
            f"Caption: {current.caption}]",
            end=" <-> "
        )

        current = current.prev

    print("None")


def insert_at_beginning(head, tail, video_id, username, caption):

    new_node = Node(video_id, username, caption)

    if head is None:
        head = new_node
        tail = new_node
        return head, tail

    new_node.next = head
    head.prev = new_node

    head = new_node

    return head, tail


def insert_at_end(head, tail, video_id, username, caption):

    new_node = Node(video_id, username, caption)

    if head is None:
        head = new_node
        tail = new_node
        return head, tail

    tail.next = new_node
    new_node.prev = tail

    tail = new_node

    return head, tail


def insert_at_position(
    head,
    tail,
    video_id,
    username,
    caption,
    position
):

    new_node = Node(video_id, username, caption)

    if position < 0:
        print("Invalid position.")
        return head, tail

    if head is None:

        if position == 0:
            return new_node, new_node

        print("Invalid position.")
        return head, tail

    if position == 0:

        new_node.next = head
        head.prev = new_node

        head = new_node

        return head, tail

    current = head
    index = 0

    while current and index < position - 1:
        current = current.next
        index += 1

    if current is None:
        print("Invalid position.")
        return head, tail

    new_node.next = current.next
    new_node.prev = current

    if current.next:
        current.next.prev = new_node
    else:
        tail = new_node

    current.next = new_node

    return head, tail


def delete_node(head, tail, video_id):

    if head is None:
        print("\nCannot delete. The TikTok list is empty.")
        return head, tail

    current = head

    while current:

        if current.video_id == video_id:

            # Delete HEAD
            if current == head:

                head = current.next

                if head:
                    head.prev = None
                else:
                    tail = None

                print(f"\nVideo ID {video_id} was deleted.")

                return head, tail

            # Delete TAIL
            if current == tail:

                tail = current.prev
                tail.next = None

                print(f"\nVideo ID {video_id} was deleted.")

                return head, tail

            # Delete MIDDLE NODE
            current.prev.next = current.next
            current.next.prev = current.prev

            print(f"\nVideo ID {video_id} was deleted.")

            return head, tail

        current = current.next

    print(f"\nVideo ID {video_id} was not found.")

    return head, tail


def search(head, video_id):

    if head is None:
        print("\nThe TikTok list is empty.")
        return

    current = head
    position = 0

    while current:

        if current.video_id == video_id:

            print("\nVideo found!")
            print(f"Position : {position}")
            print(f"Video ID : {current.video_id}")
            print(f"Username : @{current.username}")
            print(f"Caption  : {current.caption}")

            return

        current = current.next
        position += 1

    print(f"\nVideo ID {video_id} was not found.")

def load_sample_videos():

    head = None
    tail = None

    videos = [

        (
            "TT001",
            "nikolaisdump",
            "One shot Milklove au"
        ),

        (
            "TT002",
            "inkstainedmask",
            "LIES-15 wag ka ng mag sorry, hindi mo naman kasalanan na siya talaga ‘yung mahal mo #mikhaiah #mikhaiahau #pov #fiction #fyp"
        ),

        (
            "TT003",
            "nikolaisdump",
            "Milklove AU — one shot"
        ),

        (
            "TT004",
            "inkstainedmask",
            "LIES-14 — mikhaiah au #mikhaiah #mikhaiahau #pov #fiction"
        ),

        (
            "TT005",
            "nikolaisdump",
            "Milklove AU — part 2"
        ),

        (
            "TT006",
            "inkstainedmask",
            "LIES-13 — wag mo na siyang habulin #mikhaiah #mikhaiahau"
        )

    ]

    for video in videos:

        head, tail = insert_at_end(
            head,
            tail,
            video[0],
            video[1],
            video[2]
        )

    return head, tail


def menu():

    # Load videos automatically when program starts
    head, tail = load_sample_videos()

    while True:

        print("\n===================================")
        print("       TIKTOK DOUBLY LINKED LIST")
        print("===================================")

        print("1. Display Videos")
        print("2. Display Videos Backward")
        print("3. Insert at Beginning")
        print("4. Insert at End")
        print("5. Insert at Specific Position")
        print("6. Delete Video")
        print("7. Search Video")
        print("8. Exit")

        print("===================================")

        choice = input("Enter your choice: ")

        # --------------------------------
        # 1. DISPLAY
        # --------------------------------

        if choice == "1":

            traverse(head)

        # --------------------------------
        # 2. DISPLAY BACKWARD
        # --------------------------------

        elif choice == "2":

            traverse_backward(tail)

        # --------------------------------
        # 3. INSERT AT BEGINNING
        # --------------------------------

        elif choice == "3":

            video_id = input("Enter Video ID: ")
            username = input("Enter Username: ")
            caption = input("Enter Caption: ")

            head, tail = insert_at_beginning(
                head,
                tail,
                video_id,
                username,
                caption
            )

            print("\nVideo successfully inserted at the beginning!")

        # --------------------------------
        # 4. INSERT AT END
        # --------------------------------

        elif choice == "4":

            video_id = input("Enter Video ID: ")
            username = input("Enter Username: ")
            caption = input("Enter Caption: ")

            head, tail = insert_at_end(
                head,
                tail,
                video_id,
                username,
                caption
            )

            print("\nVideo successfully inserted at the end!")

        # --------------------------------
        # 5. INSERT AT POSITION
        # --------------------------------

        elif choice == "5":

            video_id = input("Enter Video ID: ")
            username = input("Enter Username: ")
            caption = input("Enter Caption: ")

            try:

                position = int(
                    input("Enter position/index: ")
                )

                head, tail = insert_at_position(
                    head,
                    tail,
                    video_id,
                    username,
                    caption,
                    position
                )

            except ValueError:

                print("\nPlease enter a valid number.")

        # --------------------------------
        # 6. DELETE
        # --------------------------------

        elif choice == "6":

            video_id = input(
                "Enter Video ID to delete: "
            )

            head, tail = delete_node(
                head,
                tail,
                video_id
            )

        # --------------------------------
        # 7. SEARCH
        # --------------------------------

        elif choice == "7":

            video_id = input(
                "Enter Video ID to search: "
            )

            search(
                head,
                video_id
            )

        # --------------------------------
        # 8. EXIT
        # --------------------------------

        elif choice == "8":

            print(
                "\nThank you for using "
                "TikTok Doubly Linked List!"
            )

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )
menu()