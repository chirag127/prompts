// """This module contains functions for getting youtube data."""


// import base64
// import contextlib
// import datetime
// import json
// import os
// import random
// import re
// import traceback

// # import Iterable
// from typing import List

// from bs4 import BeautifulSoup

// from f import (
//     WORKING_DIRECTORY,
//     append_to_file,
//     color,
//     difference_between_two_lists,
//     print_status_and_text_from_response,
//     random_choice,
//     read_from_file,
//     return_already_run_videos,
//     return_de_duped_list,
//     write_to_file,
//     write_video_id_in_cache,
// )
// from ftr import get_live_urls
// from reques import (
//     get_url,
//     get_url_with_retry,
//     get_urls,
//     get_urls_with_retry,
//     request_url,
// )


// def get_piped_api_instances() -> list:
//     """Returns the pipedapi instance."""
//     url = "https://raw.githubusercontent.com/wiki/TeamPiped/Piped-Frontend/Instances.md"

//     response = get_url(url)
//     txt = response.text
//     instances = []

//     lines = txt.split("\n")

//     lines = lines[8:]

//     for instance in lines:
//         if instance:
//             instance = instance.split("|")
//             instance = [i.strip() for i in instance]
//             instances.append(
//                 {
//                     "name": instance[0],
//                     "url": instance[1],
//                     "locations": instance[2].split(", "),
//                     "cdn": instance[3] == "Yes",
//                 }
//             )

//     all_urls = [instance["url"] for instance in instances]

//     live_urls = get_live_urls(all_urls)

//     live_instances = [
//         instance for instance in instances if instance["url"] in live_urls
//     ]

//     # sort the live instances by the order of the live urls
//     live_instances.sort(key=lambda x: live_urls.index(x["url"]))

//     return live_instances


// def get_invidious_instances_from_json():
//     """scrape domain instances from my URl"""
//     url = "https://api.invidious.io/instances.json?pretty=1&sort_by=type,users"
//     response = get_url(url)
//     instances = []
//     instances_api = []
//     if response.ok:
//         data = response.json()
//         for instance in data:
//             type_of_instance = instance[1]["type"]
//             url = instance[1]["uri"]

//             if type_of_instance == "https":
//                 instances.append(url)
//                 api = instance[1]["api"]
//                 if api:
//                     instances_api.append(url)
//     else:
//         print_status_and_text_from_response(response)

//     live_instances = get_live_urls(instances)
//     live_instances_api = get_live_urls(instances_api)

//     return live_instances, live_instances_api


// try:
//     invidious_instances, invidious_instances_api = get_invidious_instances_from_json()

//     piped_api_instances = get_piped_api_instances()

// except Exception as e:  # pylint: disable=broad-except
//     print(e)
//     traceback.print_exc()


// def not_already_run_video_ids_from_main_id_and_category(main_id, segment_category):
//     """Returns a list of video ids from the given id that have not already been run."""
//     video_ids = video_ids_from_main_id(main_id)

//     already_run_video_ids = return_already_run_videos(segment_category)

//     video_ids = [
//         video_id for video_id in video_ids if video_id not in already_run_video_ids
//     ]
//     return video_ids


// def not_already_run_video_ids_from_video_ids_and_category(
//     video_ids: List[str], segment_type: str
// ) -> List[str]:
//     """Returns a list of video ids from the
//     given list of video ids that have not already been run."""

//     already_run_video_ids = return_already_run_videos(segment_type)
//     video_ids = difference_between_two_lists(video_ids, already_run_video_ids)

//     return video_ids


// def return_video_ids_from_playlist_id_from_invidious(
//     playlist_id: str,
// ) -> List[str]:
//     """Returns a list of video ids from a playlist id."""
//     for instance in invidious_instances_api:
//         urls = [
//             f"{instance}/api/v1/playlists/{playlist_id}?page={page}"
//             for page in range(1, 2)
//         ]
//         urls = return_de_duped_list(urls)
//         responses = get_urls(urls)
//         video_ids = []
//         for response in responses:
//             if not response.ok:
//                 print_status_and_text_from_response(response)
//                 continue
//             try:
//                 data = response.json()
//                 videos = data["videos"]
//                 video_ids.extend(video["videoId"] for video in videos)
//             except Exception as error:  # pylint: disable=broad-except
//                 print(error)
//                 print(response.text)
//                 continue
//             return video_ids


// # Public innertube key (b64 encoded so that it is not incorrectly flagged)
// INNERTUBE_KEY = base64.b64decode(
//     b"QUl6YVN5QU9fRkoyU2xxVThRNFNURUhMR0NpbHdfWTlfMTFxY1c4"
// ).decode()

// YT_CONTEXT = {
//     "client": {
//         "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
//         + "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36,gzip(gfe)",
//         "clientName": "WEB",
//         "clientVersion": "2.20211221.00.00",
//     }
// }
// _YT_INITIAL_DATA_RE = (
//     r'(?:window\s*\[\s*["\']ytInitialData["\']\s*\]|'
//     + r"ytInitialData)\s*=\s*({.+?})\s*;\s*(?:var\s+meta|</script|\n)"
// )


// def get_videos_from_pl_or_c_id(channel_id, limit=False):
//     """Returns a list of videos from a channel id."""
//     continuation = None
//     videos = []

//     while True:
//         if continuation is None:
//             if channel_id.startswith("UC"):
//                 params = {"list": channel_id.replace("UC", "UU", 1)}
//             else:
//                 params = {"list": channel_id}
//             response = get_url_with_retry(
//                 "https://www.youtube.com/playlist", params=params
//             )
//             items = json.loads(re.search(_YT_INITIAL_DATA_RE, response.text)[1])[
//                 "contents"
//             ]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"][
//                 "sectionListRenderer"
//             ][
//                 "contents"
//             ][
//                 0
//             ][
//                 "itemSectionRenderer"
//             ][
//                 "contents"
//             ][
//                 0
//             ][
//                 "playlistVideoListRenderer"
//             ][
//                 "contents"
//             ]

//         else:
//             params = {"key": INNERTUBE_KEY}
//             data = {"context": YT_CONTEXT, "continuation": continuation}
//             response = request_url(
//                 "POST",
//                 "https://www.youtube.com/youtubei/v1/browse",
//                 params=params,
//                 json=data,
//             )
//             items = response.json()["onResponseReceivedActions"][0][
//                 "appendContinuationItemsAction"
//             ]["continuationItems"]

//         new_token = None
//         for vid in items:
//             if info := vid.get("playlistVideoRenderer"):
//                 videos.append(info["videoId"])
//                 continue

//             if info := vid.get("continuationItemRenderer"):
//                 new_token = info["continuationEndpoint"]["continuationCommand"]["token"]

//         if limit and len(videos) >= limit:
//             break

//         if new_token is None:
//             break
//         continuation = new_token

//     return videos


// def video_ids_from_main_id(main_id, limit=True):
//     # sourcery skip: low-code-quality
//     """
//     Returns a list of video ids from the given id. If the id is a channel or playlist,
//     it will return all videos matching that search term. If the id is a single video id,
//     it will return that single video id. If the id is an uploader url,
//     it will return all videos from that uploader's channel.
//     If the id is a piped API url, it will return all videos from that channel.
//     If the id is a fc url, it will return all videos from that uploader's channel.
//     """
//     try:
//         with contextlib.suppress(Exception):
//             os.chdir(WORKING_DIRECTORY)
//         video_ids = []

//         if (
//             main_id.startswith("user/")
//             or main_id.startswith("channel/")
//             or main_id.startswith("c/")
//             or main_id.startswith("fc/")
//             or main_id.startswith("zhannel/")
//             or main_id.startswith("h/@")
//         ):
//             channel_id = get_channel_id(main_id)
//             video_ids = video_ids_from_main_id(channel_id, limit)

//         elif (
//             main_id.startswith("PL")
//             or main_id.startswith("TL")
//             or main_id.startswith("UU")
//             or main_id.startswith("UC")
//         ):
//             if main_id.startswith("UC"):
//                 main_id = main_id.replace("UC", "UU", 1)

//             file_name = f"video_ids/{main_id}.txt"
//             if limit:
//                 video_ids = return_video_ids_from_playlist_id_from_invidious(main_id)

//                 video_ids = return_de_duped_list(video_ids)

//                 video_ids.sort()

//                 append_to_file(file_name, "\n".join(video_ids))

//             elif os.path.exists(file_name):
//                 video_ids = read_from_file(file_name).splitlines()
//                 if (
//                     datetime.datetime.now()
//                     - datetime.datetime.fromtimestamp(os.path.getmtime(file_name))
//                 ).days > 2:
//                     video_ids.extend(get_videos_from_pl_or_c_id(main_id, limit=1000))
//                 else:
//                     video_ids.extend(
//                         return_video_ids_from_playlist_id_from_invidious(main_id)
//                     )
//                 video_ids = return_de_duped_list(video_ids)
//                 video_ids.sort()

//                 write_to_file(file_name, "\n".join(video_ids))
//             else:
//                 video_ids = get_videos_from_pl_or_c_id(main_id)
//             video_ids = read_from_file(file_name).splitlines()

//         elif main_id.startswith("zearch/") or main_id.startswith("search/"):
//             main_id = main_id.replace("zearch/", "")
//             main_id = main_id.replace("search/", "")
//             video_ids = return_video_ids_from_search_with_filters(main_id)

//         elif main_id.startswith("zzearch/"):
//             if random.random() < 0.5:
//                 main_id = main_id.replace("zzearch/", "")
//                 video_ids = return_video_ids_from_search_with_filters(main_id)
//         elif main_id.startswith("trending/"):
//             main_id = main_id.replace("trending/", "")
//             video_ids = get_trending_videos(main_id)

//         elif len(main_id) == 11 and main_id.isalnum():
//             video_ids = [main_id]
//         elif main_id == "feed":
//             video_ids = get_feed()
//         elif main_id.startswith("watch?v="):
//             video_ids = [main_id.split("=")[1]]
//         elif main_id.startswith("https://youtu.be/"):
//             video_ids = [main_id.split("/")[1]]
//         else:
//             main_id = f"zearch/{main_id}"
//             video_ids = video_ids_from_main_id(main_id)
//         video_ids = return_de_duped_list(video_ids)
//         video_ids = [vid for vid in video_ids if len(vid) == 11]
//         return video_ids
//     except Exception as error:  # pylint: disable=broad-except
//         print(f"{error} in {main_id} in the function video_ids_from_main_id")
//         traceback.print_exc()
//         return []


// def return_video_ids_from_playlist_video_ids(playlist, limit=False):
//     """Returns a list of video ids from a playlist object."""

//     if limit:
//         if limit is True:
//             limit = 100
//         while playlist.hasMoreVideos and len(playlist.videos) < limit:
//             _extracted_from_return_video_ids_from_playlist_video_ids_6(playlist)
//     else:
//         while playlist.hasMoreVideos:
//             _extracted_from_return_video_ids_from_playlist_video_ids_6(playlist)
//     return [video["id"] for video in playlist.videos]


// def _extracted_from_return_video_ids_from_playlist_video_ids_6(playlist):
//     """Gets more videos from a playlist object."""
//     print("Getting more videos...")
//     playlist.getNextVideos()
//     print(f"Videos Retrieved: {len(playlist.videos)}")


// def return_invidious_search_url(
//     query,
//     page=1,
//     date="year",
//     result_type="video",
//     duration="none",
//     features="none",
//     sort="relevance",
// ):  # pylint: disable=too-many-arguments
//     """Returns a invidious search url."""
//     invidious_instance = random_choice(
//         invidious_instances
//     )

//     return (
//         f"{invidious_instance}/search?q={query}&page={page}&date={date}"
//         + f"&type={result_type}&duration={duration}&features={features}&sort={sort}"
//     )


// def return_video_ids_from_search_with_filters(
//     query,
//     date="none",
//     duration="none",
//     features="subtitles",
//     sort="views",
// ):
//     """
//     This function returns a list of video ids from a search query.
//     """

//     video_ids = []

//     number_of_pages = 2
//     random_all = 0.01
//     random_month = 0.05
//     random_week = 0.5
//     if not os.path.exists("search_video_ids"):
//         os.mkdir("search_video_ids")

//     file_name = f"search_video_ids/{query}.txt"
//     if not os.path.exists(file_name):
//         random_all = 1
//         random_week = 1
//         random_month = 1
//         number_of_pages = 10

//         write_to_file(file_name, "")

//     if random.random() < random_all:
//         number_of_pages = 3
//         video_ids = video_ids_from_invidious_urls(
//             video_ids,
//             [
//                 return_invidious_search_url(
//                     query,
//                     page,
//                     date,
//                     "video",
//                     duration,
//                     "none",
//                     "relevance",
//                 )
//                 for page in range(1, number_of_pages)
//             ],
//         )

//     if random.random() < random_month:
//         video_ids = video_ids_from_invidious_urls(
//             video_ids,
//             [
//                 return_invidious_search_url(
//                     query,
//                     page,
//                     "month",
//                     "video",
//                     duration,
//                     features,
//                     sort,
//                 )
//                 for page in range(1, number_of_pages)
//             ],
//         )
//         number_of_pages = 3

//     if random.random() < random_week:
//         video_ids.extend(
//             video_ids_from_invidious_urls(
//                 video_ids,
//                 [
//                     return_invidious_search_url(
//                         query,
//                         page,
//                         "week",
//                         "video",
//                         duration,
//                         features,
//                         sort,
//                     )
//                     for page in range(1, number_of_pages)
//                 ],
//             )
//         )

//     video_ids.extend(read_from_file(file_name).split("\n"))

//     video_ids = return_de_duped_list(video_ids)

//     write_to_file(file_name, "\n".join(video_ids))

//     return video_ids


// def video_ids_from_invidious_urls(video_ids, urls):
//     """Returns a list of video ids from a list of invidious urls."""
//     responses = get_urls_with_retry(urls, retries=3)

//     for response in responses:
//         if response.ok:
//             soup = BeautifulSoup(response.text, "html.parser")
//             video_ids.extend(
//                 a.get("href").replace("/watch?v=", "")
//                 for a in soup.find_all("a")
//                 if "listen" not in a.get("href")
//                 and a.get("href").startswith("/watch?v=")
//             )
//             video_ids.extend(video_ids)
//         else:
//             print_status_and_text_from_response(response)
//             # raise Exception("Error getting video ids from invidious urls")
//     video_ids = return_de_duped_list(video_ids)
//     return video_ids


// def return_name_from_channel_id(channel_id):
//     """Returns the name of the channel from the channel id."""
//     instances = piped_api_instances
//     for instance in instances:
//         api_instance = instance["url"]
//         url = f"{api_instance}/channels/{channel_id}"
//         response = get_url(url)

//         # check if the status_code is not starting with a 4 or 5
//         if response.ok:
//             response = response.json()
//             return response["name"]

//         print_status_and_text_from_response(response)


// def info_from_video_id(video_id, segment_type="auto", cache=False):
//     # sourcery skip: low-code-quality
//     """Returns the info of a video from its video id."""
//     try:
//         # randomize the first 4th of the instances
//         instances = random.sample(piped_api_instances, len(piped_api_instances) // 4)

//         # add the rest of the instances
//         instances.extend(piped_api_instances[len(piped_api_instances) // 4 :])

//         file_name = f"video_info/{video_id}.json"

//         if os.path.exists(file_name) and cache:
//             with open(file_name, "r") as file:
//                 return json.load(file)

//         if not os.path.exists("video_info"):
//             os.mkdir("video_info")

//         for instance in instances:
//             api_instance = instance["url"]  # pylint: disable=unsubscriptable-object
//             url = f"{api_instance}/streams/{video_id}"
//             response = request_url("GET", url)

//             if response.ok:
//                 response = response.json()

//                 if cache:
//                     if response["views"] < 100000:
//                         with open(file_name, "w") as file:
//                             json.dump({"views": response["views"]}, file)

//                     else:
//                         with open(file_name, "w") as file:
//                             json.dump(response, file)

//                 return response
//             if response.status_code == 500:
//                 do_return = True
//                 if (
//                     "This video is private" in response.text
//                     or "Video unavailable" in response.text
//                     or "This video is a paid video" in response.text
//                     or "This video has been removed" in response.text
//                     or "This live stream recording is not available" in response.text
//                     or "This video is not available in client's country"
//                     in response.text
//                     or ("ContentNotAvailableException" in response.text)
//                     or "This instance does not have a geo restriction checker"
//                     in response.text
//                 ):
//                     write_video_id_in_cache(video_id, segment_type)
//                 elif "This live event will begin" in response.text:
//                     print(f"{color.GREEN}This live event will begin.{color.END}")
//                 elif "Premieres in" in response.text:
//                     print(f"video will premiere {response.text.split('in')[1].strip()}")

//                 elif "Premiere will begin shortly" in response.text:
//                     print(f"{color.GREEN}This video will premiere shortly.{color.END}")

//                 else:
//                     print(
//                         f"{color.RED}Unknown error in video_id {video_id}.{color.END}"
//                     )
//                     print_status_and_text_from_response(response)

//                 if do_return:
//                     print_status_and_text_from_response(response)
//                     return None
//             print_status_and_text_from_response(response)

//     except Exception as error:  # pylint: disable=broad-except
//         print(f"{color.RED}Error in video_id {video_id}{color.END}")
//         print("function info_from_video_id.")
//         print(error)


// def info_from_video_id_from_invidious_api(video_id):
//     """Returns the info of a video from its video id."""
//     try:
//         file_name = f"invidious_instances/{video_id}.txt"

//         if os.path.isfile(file_name):
//             with open(file_name, "r") as file:
//                 content = file.read()

//             if content:
//                 return json.loads(content)

//         if not os.path.exists(os.path.dirname(file_name)):
//             os.makedirs(os.path.dirname(file_name))

//         for instance in invidious_instances_api:
//             api_instance = instance
//             url = f"{api_instance}/api/v1/videos/{video_id}"
//             response = get_url(url)

//             if response.ok:
//                 response = response.json()

//                 with open(file_name, "w") as file:
//                     file.write(json.dumps(response))

//                 return response
//             if response.status_code == 500:
//                 return None
//             print_status_and_text_from_response(response)

//     except Exception as error:  # pylint: disable=broad-except
//         print(f"{color.RED}Error in video_id {video_id}.{color.END}")
//         print("function info_from_video_id_from_invidious_api.")
//         print(error)


// def duration_from_video_id(video_id):
//     """Returns the duration of a video from its video id."""
//     video_info = info_from_video_id(video_id)
//     return video_info["duration"]


// def description_from_video_id(video_id):
//     """Returns the description of a video from its video id."""
//     video_info = info_from_video_id(video_id)
//     return video_info["description"]


// def get_trending_videos(region: str = "IN"):
//     """Returns the trending videos in a region. Default region is India."""
//     # Get the trending videos from the instances
//     for instance in invidious_instances_api:
//         api_instance = instance
//         url = f"{api_instance}/api/v1/trending?region={region}"
//         response = get_url(url)

//         # Return the videoIds if the response is OK
//         if response.ok:
//             response = response.json()
//             return [video["videoId"] for video in response]


// def get_channel_info(main_id):
//     """Returns the channel info from the given video id."""
//     if main_id.startswith("UC"):
//         main_id = f"channel/{main_id}"

//     for instance in piped_api_instances:
//         api_instance = instance["url"]
//         url = f"{api_instance}/{main_id}"
//         response = get_url(url)
//         if response.ok:
//             response = response.json()
//             return response
//         print_status_and_text_from_response(response)


// def get_channel_id(main_id):
//     """Returns the channel info from the given video id."""
//     if main_id.startswith("UC"):
//         return main_id
//     if main_id.startswith("channel/"):
//         return main_id.replace("channel/", "")
//     if main_id.startswith("user/") or main_id.startswith("c/"):
//         response = get_channel_info(main_id)
//         print("got channel info")
//         if response:
//             channel_id = response["id"]
//             channel_name = response["name"]
//             print(f"{main_id} {channel_name}")
//         else:
//             channel_id = "UC_gUM8rL-Lrg6O3adPW9K1g"
//             channel_name = None

//         return channel_id
//     if main_id.startswith("fc/"):
//         main_id = main_id.replace("fc/", "")
//         uploader_url = info_from_video_id(main_id)["uploaderUrl"]
//         return uploader_url.split("/")[-1]

//     if main_id.startswith("zhannel/"):
//         main_id = main_id.replace("zhannel/", "")
//         return main_id
//     if main_id.startswith("h/@"):
//         for instance in invidious_instances:
//             url = f"{instance}/{main_id.replace('h/', '')}"

//             response = get_url(url)
//             if response.ok:
//                 channel_url = response.url

//                 if channel_url.startswith(f"{instance}/channel/"):
//                     channel_id = channel_url.split("/")[-1]
//                     return channel_id
//         return main_id.replace("h/@", "zearch/")


// def get_feed():
//     """Returns the feed of the me."""
//     all_feed = []
//     for page in range(1, 11):
//         url = f"https://vid.puffyan.us/api/v1/auth/feed?max_results=10000&page={page}"
//         headers = {"Cookie": "SID=Le21gOTE-2ZwP5Y7XjVFpF8QLoA1KguEoLKHJqQsDng="}
//         response = get_url(url, headers=headers)
//         # print(response.text)
//         # print(response.status_code)

//         if response.ok:
//             response = response.json()
//             video_ids = [video["videoId"] for video in response["videos"]]

//             all_feed.extend(video_ids)
//         else:
//             print_status_and_text_from_response(response)
//             break
//     return all_feed


// def invidious_popular():
//     """Returns the popular videos from invidious instances."""
//     all_popular = []
//     for instance in invidious_instances_api:
//         api_instance = instance
//         url = f"{api_instance}/api/v1/popular"

//         response = get_url(url)
//         if response.ok:
//             response = response.json()
//             video_ids = [video["videoId"] for video in response]
//             all_popular.extend(video_ids)

//             return all_popular

//         else:
//             print_status_and_text_from_response(response)


// if __name__ == "__main__":
//     print(video_ids_from_main_id("h/@PacketPrep"))


// now we will convert the above code to javascript

import axios from 'axios';

async function get_invidious_instances_from_json() {
    let url = "https://api.invidious.io/instances.json?pretty=1&sort_by=type,users";
    // use axios to get the response
    let response = await axios.get(url);
    let instances = [];
    let instances_api = [];
    if (response.ok) {
        let data = response.json();
        for (let instance of data) {
            let type_of_instance = instance[1]["type"];
            let url = instance[1]["uri"];

            if (type_of_instance == "https") {
                instances.push(url);
                let api = instance[1]["api"];
                if (api) {
                    instances_api.push(url);
                }
            }
        }
    }
}

console.log(get_invidious_instances_from_json());