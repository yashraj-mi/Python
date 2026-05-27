from functools import reduce
from collections import defaultdict

class DataProcessor:

    def __init__(self, posts):

        self.posts = posts


    def get_titles(self):

        return [post["title"] for post in self.posts]

    def get_user_ids(self):

        return list(
            map(lambda p: p["userId"], self.posts)
        )

    
    def get_popular_posts(self, min_likes=1000):

        return list(
            filter(
                lambda p: p["likes"] >= min_likes,
                self.posts
            )
        )

    def get_most_viewed_posts(self, limit=5):

        return sorted(
            self.posts,
            key=lambda p: p["views"],
            reverse=True
        )[:limit]

    def get_viral_posts(self):

        return list(
            filter(
                lambda p:
                p["views"] > 3000
                and p["likes"] > 700,
                self.posts
            )
        )

    
    def search_posts(self, keyword):

        keyword = keyword.lower()

        return [

            post for post in self.posts

            if keyword in post["title"].lower()
            or keyword in post["content"].lower()
        ]

   
    
    def average_content_length(self):

        total = sum(
            len(post["content"])
            for post in self.posts
        )

        return total // len(self.posts)

    def longest_post(self):

        return max(
            self.posts,
            key=lambda p: len(p["content"])
        )

    

    def total_views(self):

        return reduce(
            lambda acc, p: acc + p["views"],
            self.posts,
            0
        )

    def total_likes(self):

        return reduce(
            lambda acc, p: acc + p["likes"],
            self.posts,
            0
        )

    def average_likes(self):

        return self.total_likes() // len(self.posts)


    def posts_per_user(self):

        result = defaultdict(int)

        for post in self.posts:

            user_id = post["userId"]

            result[user_id] += 1

        return dict(result)

    

    def overall_post_analysis(self):

        return {

            "total_posts": len(self.posts),

            "average_likes": self.average_likes(),

            "total_views": self.total_views(),
                        
            "average_content_length":self.average_content_length(),

            "most_viewed_post": max(
                self.posts,
                key=lambda p: p["views"]
            ),

            "most_liked_post": max(
                self.posts,
                key=lambda p: p["likes"]
            ),

            "longest_post": self.longest_post(),

        }



    def stream_posts(self):

        for post in self.posts:
            yield post
            
            