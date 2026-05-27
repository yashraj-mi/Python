from loader import load_posts
from process import DataProcessor
from db import DatabaseManager
import json


def display_menu():

    print("\n===== DATA INSIGHT ENGINE =====")

    print("1. Load Posts")
    print("2. Show Overall Analysis")
    print("3. Show Top Liked Posts")
    print("4. Search Posts")
    print("5. Show Viral Posts")
    print("6. Store Posts In Database")
    print("7. Show Database Stats")
    print("8. Generate Report")
    print("9. Exit")


def main():

    posts = []

    processor = None
    db = DatabaseManager()
    db.create_table()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            posts = load_posts()
            processor = DataProcessor(posts)
            print(f"\nLoaded {len(posts)} posts successfully.")

        elif choice == "2":

            if not processor:

                print("\nPlease load posts first.")
                continue

            analysis = processor.overall_post_analysis()

            print("\n===== OVERALL ANALYSIS =====")

            print(f"Total Posts: " f"{analysis['total_posts']}")
            print(f"Average Likes: " f"{analysis['average_likes']}")
            print(f"Total Views: " f"{analysis['total_views']}")
            print(f"Average Content Length: " f"{analysis['average_content_length']}")
            print(f"Most Viewed Post: " f"{analysis['most_viewed_post']['title']}")

        elif choice == "3":

            if not processor:

                print("\nPlease load posts first.")

                continue

            top_posts = processor.get_popular_posts()

            print("\n===== TOP LIKED POSTS =====")

            for post in top_posts[:5]:
                print(f"{post['title']} " f"(Likes: {post['likes']})")

        elif choice == "4":

            if not processor:

                print("\nPlease load posts first.")

                continue

            keyword = input("\nEnter keyword to search: ")

            results = processor.search_posts(keyword)

            print(f"\nFound {len(results)} matching posts.")

            for post in results[:5]:

                print(f"- {post['title']}")

        elif choice == "5":

            if not processor:

                print("\nPlease load posts first.")
                continue

            viral_posts = processor.get_viral_posts()

            print("\n===== VIRAL POSTS =====")

            for post in viral_posts[:5]:

                print(
                    f"{post['title']} | "
                    f"Views: {post['views']} | "
                    f"Likes: {post['likes']}"
                )

        elif choice == "6":
            if not posts:
                print("\nPlease load posts first.")

                continue
            db.insert_posts(posts)

            print("\nPosts stored in database.")

        elif choice == "7":

            stored_posts = db.fetch_all_posts()

            print("\n===== DATABASE STATS =====")
            print(f"Total Stored Posts: " f"{len(stored_posts)}")

            if stored_posts:

                print("\nFirst Stored Post:")

                print(stored_posts[0])

        elif choice == "8":
            if not processor:

                print("\nPlease load posts first.")

                continue

            report = processor.overall_post_analysis()

            with open(
                "/home/mind/Desktop/Practice/data_insight_engine/report.txt", "w"
            ) as f:
                json.dump(report, f, indent=4)

            print("\nReport generated successfully.")

        elif choice == "9":

            print("\nExiting application...")

            db.close()

            break
        else:

            print("\nInvalid choice.")


if __name__ == "__main__":

    main()
