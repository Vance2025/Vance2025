import requests
from bs4 import BeautifulSoup
import os

def extract_data(url, data_types, keywords=None):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []

        # Fetch PDFs
        if "pdf" in data_types:
            pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]
            for link in pdf_links:
                file_name = os.path.basename(link)
                results.append({
                    "File Name": file_name,
                    "Data Type": "PDF",
                    "Download Link": link,
                    "Thumbnail": "N/A"  # No thumbnail for PDFs
                })

        # Fetch photos
        if "photos" in data_types:
            photo_links = [img['src'] for img in soup.find_all('img', src=True)]
            for link in photo_links:
                file_name = os.path.basename(link)
                results.append({
                    "File Name": file_name,
                    "Data Type": "Photo",
                    "Download Link": link,
                    "Thumbnail": link  # Use the photo URL as the thumbnail
                })

        # Fetch videos
        if "video" in data_types:
            video_links = [a['href'] for a in soup.find_all('a', href=True) if any(a['href'].endswith(ext) for ext in ['.mp4', '.avi', '.mov', '.mkv'])]
            for link in video_links:
                file_name = os.path.basename(link)
                results.append({
                    "File Name": file_name,
                    "Data Type": "Video",
                    "Download Link": link,
                    "Thumbnail": link  # Use the video URL as a placeholder for the thumbnail
                })

        # Fetch keywords
        if "keywords" in data_types and keywords:
            for keyword in keywords:
                matching_links = [a['href'] for a in soup.find_all('a', href=True) if keyword.lower() in a['href'].lower()]
                for link in matching_links:
                    file_name = os.path.basename(link)
                    results.append({
                        "File Name": file_name,
                        "Data Type": f"Keyword: {keyword}",
                        "Download Link": link,
                        "Thumbnail": "N/A"  # No thumbnail for keyword-based links
                    })

        return results

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def user_input_url():
    """
    Prompts the user to input a URL and fetches data based on selected types.
    """
    url = input("Enter the URL to scrape: ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL. Please include 'http://' or 'https://'.")
        return

    print("\nSelect data types to fetch (comma-separated):")
    print("1. PDF")
    print("2. Photos")
    print("3. Video")
    print("4. Keywords")
    data_types_input = input("Enter your choices (e.g., 1,2): ").strip()
    selected_numbers = [num.strip() for num in data_types_input.split(",") if num.strip()]

    # Map numbers to data types
    data_type_map = {
        "1": "pdf",
        "2": "photos",
        "3": "video",
        "4": "keywords"
    }
    data_types = [data_type_map[num] for num in selected_numbers if num in data_type_map]

    if not data_types:
        print("No valid data types selected. Exiting.")
        return

    keywords = None
    if "keywords" in data_types:
        keywords_input = input("Enter keywords to search for (comma-separated): ").strip()
        keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]

    data = extract_data(url, data_types, keywords)
    if data:
        if len(data) == 0:
            print("\nSorry, I didn't get any data from this website. Try other data types or other websites.")
        else:
            print("\nFetched Data:")
            print(f"{'File Name':<30} {'Data Type':<20} {'Download Link':<50} {'Thumbnail'}")
            print("-" * 120)
            for item in data:
                print(f"{item['File Name']:<30} {item['Data Type']:<20} {item['Download Link']:<50} {item['Thumbnail']}")
    else:
        print("\nSorry, I didn't get any data from this website. Try other data types or other websites.")

# Example usage
if __name__ == "__main__":
    user_input_url()