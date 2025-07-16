"""A simple CLI for finding anime"""
import requests as req
from argparse import ArgumentParser

URL = "https://api.jikan.moe/v4/anime"


def get_anime_search_results(query: str, sfw: bool = True) -> list[dict]:
    res = req.get(
        f"https://api.jikan.moe/v4/anime?q={query}&sfw={str(sfw).lower()}", timeout=5)
    if res.status_code == 200:
        data = res.json()
        results = []
        for r in data["data"]:
            results.append({
                "id": r["mal_id"],
                "title": r["title"]
            })
        return results
    else:
        print(res.status_code, res.reason)


def get_cl_arguments():
    parser = ArgumentParser(description="A tool to search for anime")

    parser.add_argument("query", type=str, help="The query to search for")
    parser.add_argument("-s", "--sfw", action="store_true",
                        help="Filter out NSFW")
    parser.add_argument("-n", "--number", type=int,
                        help="The number of search results")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_cl_arguments()

    results = get_anime_search_results(args.query, args.sfw)

    results_number = results[:args.number]
    for result in results_number:
        print(result["title"])
