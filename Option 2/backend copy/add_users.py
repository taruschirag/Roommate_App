import os
import django

# Ensure settings are configured
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roommate_project.settings")
django.setup()

from users.models import User, UserImage

# New user data
new_users = [
    {
        "username": "john_doe",
        "age": 30,
        "interests": "reading, traveling",
        "preferences": "non-vegetarian",
        "images": [
            {
                "image": "https://www.hartz.com/wp-content/uploads/2022/04/small-dog-owners-1.jpg",
                "uploaded_at": "2024-06-02T00:55:02.619954Z",
            }
        ],
    },
    {
        "username": "jane_smith",
        "age": 28,
        "interests": "cooking, hiking",
        "preferences": "vegetarian",
        "images": [],
    },
]

for item in new_users:
    user = User.objects.create(
        username=item["username"],
        age=item["age"],
        interests=item["interests"],
        preferences=item["preferences"],
    )
    for image in item["images"]:
        UserImage.objects.create(
            user=user, image=image["image"], uploaded_at=image["uploaded_at"]
        )
    print(f"Successfully added user {user.username}")
