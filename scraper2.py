#!/usr/bin/env python

__author__ = 'Sarah Beverton'

import re
import sys
import argparse
import requests
from bs4 import BeautifulSoup


def scrape_urls(webpage):
    """Finds all URLs from a web page"""
    html = requests.get(webpage)
    urls = []
    pattern = r"""
        http[s]?://(?:[a-zA-Z]|
        [0-9]|[$-_@.&+]|[!*\(\),]|
        (?:%[0-9a-fA-F][0-9a-fA-F]))+"""
    url_regex = re.compile(pattern, re.VERBOSE)
    urls = url_regex.findall(html.text)
    return urls


def scrape_images(webpage):
    """Finds image sources and returns their urls"""
    html = requests.get(webpage)
    images = []
    soup = BeautifulSoup(html.text, 'html.parser')
    for img in soup.find_all('img'):
        img_url = img['src']
        img_full_url = webpage + img_url
        images.append(img_full_url)
    return images


def scrape_links(webpage):
    """Finds a href links and returns them"""
    html = requests.get(webpage)
    links = []
    soup = BeautifulSoup(html.text, 'html.parser')
    http_pattern = r'http\S+'
    http_regex = re.compile(http_pattern)
    for a in soup.find_all('a'):
        a_url = a['href']
        if http_regex.search(a_url):
            links.append(a_url)
        else:
            links.append(webpage + a_url)
    return links


def scrape_emails(webpage):
    """Finds all emails from a web page"""
    emails = []
    html = requests.get(webpage)
    email_regex = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+')
    emails = email_regex.findall(html.text)
    return emails


def scrape_phones(webpage):
    """Finds all phone numbers from a web page"""
    phones = []
    html = requests.get(webpage)
    phone_regex = re.compile(r'\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}')
    phones = phone_regex.findall(html.text)
    return phones


def create_parser():
    """Creates an argument parser object."""
    parser = argparse.ArgumentParser()
    parser.add_argument('webpage', help='webpage to search')

    return parser


def main(args):
    """Parses args, scans webpages"""
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    urls = scrape_urls(parsed_args.webpage)
    emails = scrape_emails(parsed_args.webpage)
    phones = scrape_phones(parsed_args.webpage)
    images = scrape_images(parsed_args.webpage)
    links = scrape_links(parsed_args.webpage)

    all_urls = urls+images+links
    all_urls_set = set(all_urls)

    if all_urls:
        print("\nURLS:\n\n", '\n'.join(all_urls_set))
    else:
        print("\nURLS:\n\nNone")

    if emails:
        print("\nEMAILS:\n\n", '\n'.join(emails))
    else:
        print("\nEMAILS:\n\nNone")

    if phones:
        print("\nPHONE NUMBERS:\n\n", '\n'.join(phones))
    else:
        print("\nPHONE NUMBERS:\n\nNone")


if __name__ == '__main__':
    main(sys.argv[1:])
