#!/usr/bin/env python3
"""ResizeNow Build — Social Media Image Resizer"""

import os, json, random
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DOMAIN = "resizenow.net"
OUTPUT = "."

def w(path, content):
    full = os.path.join(OUTPUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ═══ Platform Presets ═══════════════════════════════
PRESETS = {
    "instagram-post": {"name": "Instagram Post", "width": 1080, "height": 1080, "platform": "Instagram", "ratio": "1:1"},
    "instagram-story": {"name": "Instagram Story", "width": 1080, "height": 1920, "platform": "Instagram", "ratio": "9:16"},
    "instagram-reel": {"name": "Instagram Reel Cover", "width": 1080, "height": 1920, "platform": "Instagram", "ratio": "9:16"},
    "instagram-profile": {"name": "Instagram Profile", "width": 320, "height": 320, "platform": "Instagram", "ratio": "1:1"},
    "instagram-carousel": {"name": "Instagram Carousel", "width": 1080, "height": 1080, "platform": "Instagram", "ratio": "1:1"},
    "tiktok-video": {"name": "TikTok Video", "width": 1080, "height": 1920, "platform": "TikTok", "ratio": "9:16"},
    "tiktok-profile": {"name": "TikTok Profile", "width": 200, "height": 200, "platform": "TikTok", "ratio": "1:1"},
    "tiktok-cover": {"name": "TikTok Cover", "width": 1080, "height": 1920, "platform": "TikTok", "ratio": "9:16"},
    "youtube-thumbnail": {"name": "YouTube Thumbnail", "width": 1280, "height": 720, "platform": "YouTube", "ratio": "16:9"},
    "youtube-banner": {"name": "YouTube Banner", "width": 2560, "height": 1440, "platform": "YouTube", "ratio": "16:9"},
    "youtube-profile": {"name": "YouTube Profile", "width": 800, "height": 800, "platform": "YouTube", "ratio": "1:1"},
    "youtube-shorts": {"name": "YouTube Shorts", "width": 1080, "height": 1920, "platform": "YouTube", "ratio": "9:16"},
    "discord-avatar": {"name": "Discord Avatar", "width": 512, "height": 512, "platform": "Discord", "ratio": "1:1"},
    "discord-banner": {"name": "Discord Banner", "width": 680, "height": 240, "platform": "Discord", "ratio": "2.83:1"},
    "discord-server-icon": {"name": "Discord Server Icon", "width": 512, "height": 512, "platform": "Discord", "ratio": "1:1"},
    "discord-emoji": {"name": "Discord Emoji", "width": 128, "height": 128, "platform": "Discord", "ratio": "1:1"},
    "linkedin-banner": {"name": "LinkedIn Banner", "width": 1584, "height": 396, "platform": "LinkedIn", "ratio": "4:1"},
    "linkedin-profile": {"name": "LinkedIn Profile", "width": 400, "height": 400, "platform": "LinkedIn", "ratio": "1:1"},
    "linkedin-post": {"name": "LinkedIn Post", "width": 1200, "height": 627, "platform": "LinkedIn", "ratio": "1.91:1"},
    "linkedin-company-logo": {"name": "LinkedIn Company Logo", "width": 300, "height": 300, "platform": "LinkedIn", "ratio": "1:1"},
    "facebook-cover": {"name": "Facebook Cover", "width": 820, "height": 312, "platform": "Facebook", "ratio": "2.63:1"},
    "facebook-profile": {"name": "Facebook Profile", "width": 170, "height": 170, "platform": "Facebook", "ratio": "1:1"},
    "facebook-post": {"name": "Facebook Post", "width": 1200, "height": 630, "platform": "Facebook", "ratio": "1.91:1"},
    "facebook-event": {"name": "Facebook Event", "width": 1920, "height": 1005, "platform": "Facebook", "ratio": "1.91:1"},
    "twitter-header": {"name": "X Header", "width": 1500, "height": 500, "platform": "X", "ratio": "3:1"},
    "twitter-post": {"name": "X Post", "width": 1200, "height": 675, "platform": "X", "ratio": "16:9"},
    "twitter-profile": {"name": "X Profile", "width": 400, "height": 400, "platform": "X", "ratio": "1:1"},
    "pinterest-pin": {"name": "Pinterest Pin", "width": 1000, "height": 1500, "platform": "Pinterest", "ratio": "2:3"},
    "pinterest-profile": {"name": "Pinterest Profile", "width": 165, "height": 165, "platform": "Pinterest", "ratio": "1:1"},
    "pinterest-board": {"name": "Pinterest Board", "width": 222, "height": 150, "platform": "Pinterest", "ratio": "1.48:1"},
    "whatsapp-profile": {"name": "WhatsApp Profile", "width": 500, "height": 500, "platform": "WhatsApp", "ratio": "1:1"},
    "whatsapp-status": {"name": "WhatsApp Status", "width": 1080, "height": 1920, "platform": "WhatsApp", "ratio": "9:16"},
    "snapchat-icon": {"name": "Snapchat Icon", "width": 320, "height": 320, "platform": "Snapchat", "ratio": "1:1"},
    "snapchat-story": {"name": "Snapchat Story", "width": 1080, "height": 1920, "platform": "Snapchat", "ratio": "9:16"},
}

# ═══ Page Definitions ═══════════════════════════════

# Platform main pages
PLATFORM_PAGES = [
    {"slug": "resize-image-for-instagram", "title": "Resize Image for Instagram — Free Online Tool", "desc": "Resize images for Instagram posts, stories, reels, and profiles. Perfect dimensions every time. Free, browser-based.", "platform": "instagram"},
    {"slug": "resize-image-for-tiktok", "title": "Resize Image for TikTok — Free Online Tool", "desc": "Resize images for TikTok videos, covers, and profiles. Free, browser-based, instant.", "platform": "tiktok"},
    {"slug": "resize-image-for-youtube", "title": "Resize Image for YouTube — Free Online Tool", "desc": "Resize images for YouTube thumbnails, banners, and profiles. Free, browser-based, instant.", "platform": "youtube"},
    {"slug": "resize-image-for-discord", "title": "Resize Image for Discord — Free Online Tool", "desc": "Resize images for Discord avatars, banners, and server icons. Free, browser-based, instant.", "platform": "discord"},
    {"slug": "resize-image-for-linkedin", "title": "Resize Image for LinkedIn — Free Online Tool", "desc": "Resize images for LinkedIn banners, profiles, and posts. Free, browser-based, instant.", "platform": "linkedin"},
    {"slug": "resize-image-for-facebook", "title": "Resize Image for Facebook — Free Online Tool", "desc": "Resize images for Facebook covers, profiles, and posts. Free, browser-based, instant.", "platform": "facebook"},
    {"slug": "resize-image-for-twitter", "title": "Resize Image for X/Twitter — Free Online Tool", "desc": "Resize images for X/Twitter headers, posts, and profiles. Free, browser-based, instant.", "platform": "twitter"},
    {"slug": "resize-image-for-pinterest", "title": "Resize Image for Pinterest — Free Online Tool", "desc": "Resize images for Pinterest pins and profiles. Free, browser-based, instant.", "platform": "pinterest"},
    {"slug": "resize-image-for-whatsapp", "title": "Resize Image for WhatsApp — Free Online Tool", "desc": "Resize images for WhatsApp profiles and status. Free, browser-based, instant.", "platform": "whatsapp"},
    {"slug": "resize-image-for-snapchat", "title": "Resize Image for Snapchat — Free Online Tool", "desc": "Resize images for Snapchat icons and stories. Free, browser-based, instant.", "platform": "snapchat"},
]

# Instagram sub-pages
INSTAGRAM_PAGES = [
    {"slug": "instagram-post-size", "title": "Instagram Post Size — Dimensions & Guide 2026", "desc": "Instagram post size is 1080x1080 pixels (1:1 ratio). Complete guide with templates and tips.", "platform": "instagram"},
    {"slug": "instagram-story-size", "title": "Instagram Story Size — Dimensions & Guide 2026", "desc": "Instagram story size is 1080x1920 pixels (9:16 ratio). Complete guide with examples.", "platform": "instagram"},
    {"slug": "instagram-reel-cover-size", "title": "Instagram Reel Cover Size — Dimensions & Guide", "desc": "Instagram reel cover size is 1080x1920 pixels. How to create the perfect reel cover.", "platform": "instagram"},
    {"slug": "instagram-profile-picture-size", "title": "Instagram Profile Picture Size — Dimensions & Guide", "desc": "Instagram profile picture size is 320x320 pixels. Tips for a perfect profile photo.", "platform": "instagram"},
    {"slug": "instagram-carousel-size", "title": "Instagram Carousel Size — Dimensions & Guide", "desc": "Instagram carousel size is 1080x1080 or 1080x1350 pixels. Best practices for carousels.", "platform": "instagram"},
    {"slug": "resize-image-for-instagram-post", "title": "Resize Image for Instagram Post — Free Tool", "desc": "Resize any image to Instagram post dimensions (1080x1080). Free, instant.", "platform": "instagram"},
    {"slug": "resize-image-for-instagram-story", "title": "Resize Image for Instagram Story — Free Tool", "desc": "Resize any image to Instagram story dimensions (1080x1920). Free, instant.", "platform": "instagram"},
    {"slug": "resize-image-for-instagram-reel", "title": "Resize Image for Instagram Reel — Free Tool", "desc": "Resize any image to Instagram reel cover dimensions. Free, instant.", "platform": "instagram"},
    {"slug": "instagram-image-size-guide", "title": "Instagram Image Size Guide — All Dimensions 2026", "desc": "Complete Instagram image size guide: posts, stories, reels, profiles, carousels.", "platform": "instagram"},
    {"slug": "instagram-photo-resizer", "title": "Instagram Photo Resizer — Free Online Tool", "desc": "Resize photos for any Instagram format. Free, browser-based, instant.", "platform": "instagram"},
]

# Discord sub-pages
DISCORD_PAGES = [
    {"slug": "discord-avatar-size", "title": "Discord Avatar Size — Dimensions & Guide", "desc": "Discord avatar size is 512x512 pixels. How to create the perfect Discord avatar.", "platform": "discord"},
    {"slug": "discord-banner-size", "title": "Discord Banner Size — Dimensions & Guide", "desc": "Discord banner size is 680x240 pixels. Tips for a stunning Discord banner.", "platform": "discord"},
    {"slug": "discord-server-icon-size", "title": "Discord Server Icon Size — Dimensions & Guide", "desc": "Discord server icon size is 512x512 pixels. Best practices for server icons.", "platform": "discord"},
    {"slug": "discord-emoji-size", "title": "Discord Emoji Size — Dimensions & Guide", "desc": "Discord emoji size is 128x128 pixels. How to create custom Discord emojis.", "platform": "discord"},
    {"slug": "resize-image-for-discord-avatar", "title": "Resize Image for Discord Avatar — Free Tool", "desc": "Resize any image to Discord avatar dimensions (512x512). Free, instant.", "platform": "discord"},
    {"slug": "resize-image-for-discord-banner", "title": "Resize Image for Discord Banner — Free Tool", "desc": "Resize any image to Discord banner dimensions (680x240). Free, instant.", "platform": "discord"},
    {"slug": "discord-image-size-guide", "title": "Discord Image Size Guide — All Dimensions 2026", "desc": "Complete Discord image size guide: avatars, banners, server icons, emojis.", "platform": "discord"},
    {"slug": "discord-photo-resizer", "title": "Discord Photo Resizer — Free Online Tool", "desc": "Resize photos for any Discord format. Free, browser-based, instant.", "platform": "discord"},
]

# YouTube sub-pages
YOUTUBE_PAGES = [
    {"slug": "youtube-thumbnail-size", "title": "YouTube Thumbnail Size — Dimensions & Guide 2026", "desc": "YouTube thumbnail size is 1280x720 pixels (16:9). How to create clickable thumbnails.", "platform": "youtube"},
    {"slug": "youtube-banner-size", "title": "YouTube Banner Size 2026: 2560×1440 px Guide | ResizeNow", "desc": "YouTube banner size is 2560×1440 pixels (16:9). Safe area is 1546×423 px. Design tips and templates.", "platform": "youtube"},
    {"slug": "youtube-channel-icon-size", "title": "YouTube Channel Icon Size — Dimensions & Guide", "desc": "YouTube channel icon size is 800x800 pixels. Tips for a professional icon.", "platform": "youtube"},
    {"slug": "youtube-shorts-thumbnail-size", "title": "YouTube Shorts Thumbnail Size — Dimensions & Guide", "desc": "YouTube Shorts thumbnail size is 1080x1920 pixels (9:16).", "platform": "youtube"},
    {"slug": "resize-image-for-youtube-thumbnail", "title": "Resize Image for YouTube Thumbnail — Free Tool", "desc": "Resize any image to YouTube thumbnail dimensions (1280x720). Free, instant.", "platform": "youtube"},
    {"slug": "resize-image-for-youtube-banner", "title": "Resize Image for YouTube Banner — Free Tool", "desc": "Resize any image to YouTube banner dimensions (2560x1440). Free, instant.", "platform": "youtube"},
    {"slug": "youtube-image-size-guide", "title": "YouTube Image Size Guide — All Dimensions 2026", "desc": "Complete YouTube image size guide: thumbnails, banners, channel icons, Shorts.", "platform": "youtube"},
    {"slug": "youtube-photo-resizer", "title": "YouTube Photo Resizer — Free Online Tool", "desc": "Resize photos for any YouTube format. Free, browser-based, instant.", "platform": "youtube"},
]

# LinkedIn sub-pages
LINKEDIN_PAGES = [
    {"slug": "linkedin-banner-size", "title": "LinkedIn Banner Size — Dimensions & Guide 2026", "desc": "LinkedIn banner size is 1584x396 pixels. Tips for a professional banner.", "platform": "linkedin"},
    {"slug": "linkedin-profile-picture-size", "title": "LinkedIn Profile Picture Size — Dimensions & Guide", "desc": "LinkedIn profile picture size is 400x400 pixels. Tips for a professional photo.", "platform": "linkedin"},
    {"slug": "linkedin-post-image-size", "title": "LinkedIn Post Image Size 2026: 1200×627 px Guide | ResizeNow", "desc": "LinkedIn post image size is 1200×627 pixels (1.91:1 ratio). Best practices for maximum engagement in 2026.", "platform": "linkedin"},
    {"slug": "resize-image-for-linkedin-banner", "title": "Resize Image for LinkedIn Banner — Free Tool", "desc": "Resize any image to LinkedIn banner dimensions (1584x396). Free, instant.", "platform": "linkedin"},
    {"slug": "linkedin-image-size-guide", "title": "LinkedIn Image Size Guide — All Dimensions 2026", "desc": "Complete LinkedIn image size guide: banners, profiles, posts, company logos.", "platform": "linkedin"},
    {"slug": "linkedin-photo-resizer", "title": "LinkedIn Photo Resizer — Free Online Tool", "desc": "Resize photos for any LinkedIn format. Free, browser-based, instant.", "platform": "linkedin"},
]

# TikTok sub-pages
TIKTOK_PAGES = [
    {"slug": "tiktok-video-size", "title": "TikTok Video Size — Dimensions & Guide 2026", "desc": "TikTok video size is 1080x1920 pixels (9:16). Complete guide for viral videos.", "platform": "tiktok"},
    {"slug": "tiktok-profile-picture-size", "title": "TikTok Profile Picture Size — Dimensions & Guide", "desc": "TikTok profile picture size is 200x200 pixels. Tips for a standout profile.", "platform": "tiktok"},
    {"slug": "tiktok-cover-size", "title": "TikTok Cover Size 2026: 1080×1920 px Guide | ResizeNow", "desc": "TikTok cover size is 1080×1920 pixels (9:16). How to create an eye-catching cover that gets clicks.", "platform": "tiktok"},
    {"slug": "resize-image-for-tiktok-video", "title": "Resize Image for TikTok Video — Free Tool", "desc": "Resize any image to TikTok video dimensions (1080x1920). Free, instant.", "platform": "tiktok"},
    {"slug": "tiktok-image-size-guide", "title": "TikTok Image Size Guide — All Dimensions 2026", "desc": "Complete TikTok image size guide: videos, profiles, covers.", "platform": "tiktok"},
    {"slug": "tiktok-photo-resizer", "title": "TikTok Photo Resizer — Free Online Tool", "desc": "Resize photos for any TikTok format. Free, browser-based, instant.", "platform": "tiktok"},
]

# Facebook sub-pages
FACEBOOK_PAGES = [
    {"slug": "facebook-cover-size", "title": "Facebook Cover Size — Dimensions & Guide 2026", "desc": "Facebook cover size is 820x312 pixels. Tips for a stunning cover photo.", "platform": "facebook"},
    {"slug": "facebook-profile-picture-size", "title": "Facebook Profile Picture Size — Dimensions & Guide", "desc": "Facebook profile picture size is 170x170 pixels. Tips for a perfect profile.", "platform": "facebook"},
    {"slug": "facebook-post-image-size", "title": "Facebook Post Image Size — Dimensions & Guide", "desc": "Facebook post image size is 1200x630 pixels. Best practices for engagement.", "platform": "facebook"},
    {"slug": "resize-image-for-facebook-cover", "title": "Resize Image for Facebook Cover — Free Tool", "desc": "Resize any image to Facebook cover dimensions (820x312). Free, instant.", "platform": "facebook"},
    {"slug": "facebook-image-size-guide", "title": "Facebook Image Size Guide — All Dimensions 2026", "desc": "Complete Facebook image size guide: covers, profiles, posts, events.", "platform": "facebook"},
    {"slug": "facebook-photo-resizer", "title": "Facebook Photo Resizer — Free Online Tool", "desc": "Resize photos for any Facebook format. Free, browser-based, instant.", "platform": "facebook"},
]

# X/Twitter sub-pages
TWITTER_PAGES = [
    {"slug": "twitter-header-size", "title": "X/Twitter Header Size — Dimensions & Guide 2026", "desc": "X/Twitter header size is 1500x500 pixels. Tips for a professional header.", "platform": "twitter"},
    {"slug": "twitter-post-image-size", "title": "X/Twitter Post Image Size — Dimensions & Guide", "desc": "X/Twitter post image size is 1200x675 pixels. Best practices for engagement.", "platform": "twitter"},
    {"slug": "twitter-profile-picture-size", "title": "X/Twitter Profile Picture Size 2026: 400×400 px Guide | ResizeNow", "desc": "X/Twitter profile picture size is 400×400 pixels (1:1). Tips for a standout profile photo in 2026.", "platform": "twitter"},
    {"slug": "resize-image-for-twitter-header", "title": "Resize Image for X/Twitter Header — Free Tool", "desc": "Resize any image to X/Twitter header dimensions (1500x500). Free, instant.", "platform": "twitter"},
    {"slug": "twitter-image-size-guide", "title": "X/Twitter Image Size Guide — All Dimensions 2026", "desc": "Complete X/Twitter image size guide: headers, posts, profiles.", "platform": "twitter"},
    {"slug": "twitter-photo-resizer", "title": "X/Twitter Photo Resizer — Free Online Tool", "desc": "Resize photos for any X/Twitter format. Free, browser-based, instant.", "platform": "twitter"},
]

# Pinterest sub-pages
PINTEREST_PAGES = [
    {"slug": "pinterest-pin-size", "title": "Pinterest Pin Size — Dimensions & Guide 2026", "desc": "Pinterest pin size is 1000x1500 pixels (2:3 ratio). How to create viral pins.", "platform": "pinterest"},
    {"slug": "pinterest-profile-picture-size", "title": "Pinterest Profile Picture Size — Dimensions & Guide", "desc": "Pinterest profile picture size is 165x165 pixels.", "platform": "pinterest"},
    {"slug": "resize-image-for-pinterest-pin", "title": "Resize Image for Pinterest Pin — Free Tool", "desc": "Resize any image to Pinterest pin dimensions (1000x1500). Free, instant.", "platform": "pinterest"},
    {"slug": "pinterest-image-size-guide", "title": "Pinterest Image Size Guide — All Dimensions 2026", "desc": "Complete Pinterest image size guide: pins, profiles, boards.", "platform": "pinterest"},
]

# WhatsApp sub-pages
WHATSAPP_PAGES = [
    {"slug": "whatsapp-profile-picture-size", "title": "WhatsApp Profile Picture Size — Dimensions & Guide", "desc": "WhatsApp profile picture size is 500x500 pixels. Tips for a perfect profile.", "platform": "whatsapp"},
    {"slug": "whatsapp-status-size", "title": "WhatsApp Status Size — Dimensions & Guide", "desc": "WhatsApp status size is 1080x1920 pixels (9:16).", "platform": "whatsapp"},
    {"slug": "resize-image-for-whatsapp-profile", "title": "Resize Image for WhatsApp Profile — Free Tool", "desc": "Resize any image to WhatsApp profile dimensions (500x500). Free, instant.", "platform": "whatsapp"},
    {"slug": "whatsapp-image-size-guide", "title": "WhatsApp Image Size Guide — All Dimensions 2026", "desc": "Complete WhatsApp image size guide: profiles, status, broadcasts.", "platform": "whatsapp"},
]

# Generic pages — core tools
GENERIC_PAGES = [
    # Primary: differentiated by intent
    {"slug": "image-resizer", "title": "Image Resizer — Free Online Tool (No Signup)", "desc": "Resize any image online for free. Support PNG, JPG, WebP. Browser-based, instant, no signup required.", "platform": "generic"},
    {"slug": "photo-resizer", "title": "Photo Resizer for Social Media — Free Online", "desc": "Resize photos for social media: Instagram, Facebook, X, LinkedIn. Free instant tool with platform presets.", "platform": "generic"},
    {"slug": "picture-resizer", "title": "Picture Resizer — Resize for Web & Email Free", "desc": "Resize pictures for websites, email attachments, and documents. Free, instant, no upload needed.", "platform": "generic"},
    {"slug": "image-resize-online", "title": "Resize Image Online — Any Size, Any Format, Free", "desc": "Resize images online in pixels, percentage, or custom dimensions. PNG, JPG, WebP support. Free & instant.", "platform": "generic"},
    {"slug": "resize-photo-online", "title": "Resize Photos Online — Free Tool for Any Platform", "desc": "Resize photos online for Instagram, websites, printing, and more. No signup, no watermark.", "platform": "generic"},
    # Tools
    {"slug": "image-crop-tool", "title": "Image Crop Tool — Free Online", "desc": "Crop images online for free. Visual crop with aspect ratio lock.", "platform": "generic"},
    {"slug": "aspect-ratio-calculator", "title": "Aspect Ratio Calculator — Free Online Tool", "desc": "Calculate aspect ratios for any image. Free, instant.", "platform": "generic"},
    {"slug": "bulk-image-resizer", "title": "Bulk Image Resizer — Resize Multiple Images Free", "desc": "Resize multiple images at once. Free, browser-based, instant.", "platform": "generic"},
    # NEW: GSC-query-driven long-tail pages（2026-06-14）
    {"slug": "social-media-image-dimensions", "title": "Social Media Image Dimensions 2026 — All Platforms Guide", "desc": "Complete guide to social media image dimensions: Instagram, Facebook, LinkedIn, X/Twitter, YouTube, TikTok, Pinterest, and more. Updated for 2026.", "platform": "social-media-dimensions"},
    {"slug": "resize-image-for-printing", "title": "Resize Image for Printing — DPI & Dimensions Guide", "desc": "Resize images for high-quality printing. Set DPI, inches, or centimeters. Free online tool for print-ready images.", "platform": "printing"},
    {"slug": "change-image-resolution", "title": "Change Image Resolution Online — Free Tool", "desc": "Change the resolution of any image online. Adjust DPI, pixels per inch, or total pixel count. Free, instant.", "platform": "resolution"},
    {"slug": "image-size-guide", "title": "Image Size Guide 2026 — All Social Media & Web Dimensions", "desc": "Ultimate image size guide for every platform. Social media, web banners, email headers, and more. All dimensions in one place.", "platform": "image-size-guide"},
    {"slug": "resize-jpg-online", "title": "Resize JPG Online — Free JPG Image Resizer", "desc": "Resize JPG images online for free. Reduce or enlarge JPG dimensions. No quality loss. Instant, browser-based.", "platform": "generic"},
    {"slug": "free-online-image-resizer", "title": "Free Online Image Resizer — No Signup, No Watermark", "desc": "100% free online image resizer. No signup, no watermark, no limits. Resize images instantly in your browser.", "platform": "generic"},
]

# Combine all pages
ALL_SCENARIOS = (
    PLATFORM_PAGES +
    INSTAGRAM_PAGES +
    DISCORD_PAGES +
    YOUTUBE_PAGES +
    LINKEDIN_PAGES +
    TIKTOK_PAGES +
    FACEBOOK_PAGES +
    TWITTER_PAGES +
    PINTEREST_PAGES +
    WHATSAPP_PAGES +
    GENERIC_PAGES
)

# ═══ Enrichment Content ═════════════════════════════

PLATFORM_DATA = {
    "instagram": {
        "name": "Instagram",
        "about": "Instagram supports multiple image formats with different dimensions. Using the correct size ensures your photos look sharp and professional. Instagram automatically crops images that don't match the required dimensions, which can cut off important parts of your photo.",
        "sizes": [
            ("Post (Square)", "1080 x 1080", "1:1"),
            ("Post (Portrait)", "1080 x 1350", "4:5"),
            ("Story", "1080 x 1920", "9:16"),
            ("Reel Cover", "1080 x 1920", "9:16"),
            ("Profile Picture", "320 x 320", "1:1"),
            ("Carousel", "1080 x 1080 or 1080 x 1350", "1:1 or 4:5"),
        ],
        "faq": [
            ("What size should Instagram posts be?", "Instagram posts should be 1080x1080 pixels (square) or 1080x1350 pixels (portrait). Portrait images take up more screen space and tend to get more engagement."),
            ("What size should Instagram stories be?", "Instagram stories should be 1080x1920 pixels (9:16 ratio). This fills the entire phone screen for an immersive experience."),
            ("What happens if I upload the wrong size?", "Instagram will automatically crop your image to fit, which may cut off important parts. Always resize to the recommended dimensions first."),
            ("What's the best format for Instagram?", "JPG is recommended for photos, PNG for graphics with text or transparency. Instagram compresses all uploads, so start with high quality."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select an Instagram preset (Post, Story, Reel, or Profile)",
            "Preview the resized image and adjust if needed",
            "Download and upload to Instagram",
        ],
        "tips": "Portrait images (4:5 ratio) take up 20% more screen space than square images, leading to higher engagement. For stories, keep important content in the center to avoid being cut off by UI elements.",
    },
    "discord": {
        "name": "Discord",
        "about": "Discord uses different image sizes for avatars, banners, server icons, and emojis. Using the correct dimensions ensures your images look crisp on both desktop and mobile. Discord supports PNG, JPG, GIF, and WebP formats.",
        "sizes": [
            ("Avatar", "512 x 512", "1:1"),
            ("Banner", "680 x 240", "2.83:1"),
            ("Server Icon", "512 x 512", "1:1"),
            ("Emoji", "128 x 128", "1:1"),
            ("Server Banner", "960 x 540", "16:9"),
        ],
        "faq": [
            ("What size should a Discord avatar be?", "Discord avatars should be 512x512 pixels. Discord displays them as circles, so keep important content in the center."),
            ("What size should a Discord banner be?", "Discord banners should be 680x240 pixels. This is for Nitro users only."),
            ("What size should Discord emojis be?", "Discord emojis should be 128x128 pixels. They're displayed at much smaller sizes, so keep designs simple."),
            ("What formats does Discord support?", "Discord supports PNG, JPG, GIF, and WebP. GIF is recommended for animated avatars and emojis."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a Discord preset (Avatar, Banner, Server Icon, or Emoji)",
            "Preview the resized image",
            "Download and upload to Discord",
        ],
        "tips": "Discord displays avatars as circles, so keep important content centered. For server icons, simple designs work best as they're displayed very small in the server list.",
    },
    "youtube": {
        "name": "YouTube",
        "about": "YouTube uses different image sizes for thumbnails, channel banners, and profile pictures. Thumbnails are especially important as they directly impact click-through rates. Using the correct dimensions ensures your content looks professional across all devices.",
        "sizes": [
            ("Thumbnail", "1280 x 720", "16:9"),
            ("Channel Banner", "2560 x 1440", "16:9"),
            ("Channel Icon", "800 x 800", "1:1"),
            ("Shorts Thumbnail", "1080 x 1920", "9:16"),
        ],
        "faq": [
            ("What size should YouTube thumbnails be?", "YouTube thumbnails should be 1280x720 pixels (16:9 ratio). This is the most important image for video click-through rates."),
            ("What size should a YouTube banner be?", "YouTube channel banners should be 2560x1440 pixels. The safe area for text is 1546x423 pixels in the center."),
            ("Can I change my thumbnail after uploading?", "Yes, you can change thumbnails at any time in YouTube Studio."),
            ("What's the best format for thumbnails?", "JPG is recommended for thumbnails. Keep file size under 2MB for fast loading."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a YouTube preset (Thumbnail, Banner, or Channel Icon)",
            "Preview the resized image",
            "Download and upload to YouTube Studio",
        ],
        "tips": "Thumbnails with faces get 38% more clicks. Use high contrast, large text (readable on mobile), and expressive facial expressions. The safe area for channel banners is the center 1546x423 pixels.",
    },
    "linkedin": {
        "name": "LinkedIn",
        "about": "LinkedIn uses different image sizes for profile pictures, banners, and post images. Professional images are especially important on LinkedIn as it's a career-focused platform. Using the correct dimensions ensures your profile looks polished and professional.",
        "sizes": [
            ("Banner", "1584 x 396", "4:1"),
            ("Profile Picture", "400 x 400", "1:1"),
            ("Post Image", "1200 x 627", "1.91:1"),
            ("Company Logo", "300 x 300", "1:1"),
            ("Company Cover", "1128 x 191", "5.9:1"),
        ],
        "faq": [
            ("What size should a LinkedIn profile picture be?", "LinkedIn profile pictures should be 400x400 pixels. Professional headshots work best."),
            ("What size should a LinkedIn banner be?", "LinkedIn banners should be 1584x396 pixels. Use this space to showcase your expertise or brand."),
            ("What size should LinkedIn post images be?", "LinkedIn post images should be 1200x627 pixels for optimal display in the feed."),
            ("What's the best format for LinkedIn?", "JPG is recommended for photos, PNG for graphics with text or logos."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a LinkedIn preset (Banner, Profile, or Post)",
            "Preview the resized image",
            "Download and upload to LinkedIn",
        ],
        "tips": "LinkedIn is a professional platform, so use high-quality, professional images. For banners, showcase your expertise, industry, or personal brand. For profile pictures, use a professional headshot with good lighting.",
    },
    "tiktok": {
        "name": "TikTok",
        "about": "TikTok uses vertical video format (9:16 ratio) as its primary format. Profile pictures and cover images also have specific dimensions. Using the correct sizes ensures your content looks great on the platform.",
        "sizes": [
            ("Video", "1080 x 1920", "9:16"),
            ("Profile Picture", "200 x 200", "1:1"),
            ("Cover", "1080 x 1920", "9:16"),
        ],
        "faq": [
            ("What size should TikTok videos be?", "TikTok videos should be 1080x1920 pixels (9:16 ratio). This fills the entire phone screen."),
            ("What size should a TikTok profile picture be?", "TikTok profile pictures should be 200x200 pixels. They're displayed as circles."),
            ("What's the best format for TikTok?", "JPG for images, MP4 for videos. Keep images under 10MB for fast uploads."),
            ("Can I upload horizontal videos?", "You can, but they'll have black bars above and below. Vertical (9:16) is strongly recommended."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a TikTok preset (Video, Profile, or Cover)",
            "Preview the resized image",
            "Download and upload to TikTok",
        ],
        "tips": "TikTok is a vertical-first platform. Always use 9:16 ratio for videos and covers. For profile pictures, keep designs simple as they're displayed very small.",
    },
    "facebook": {
        "name": "Facebook",
        "about": "Facebook uses different image sizes for cover photos, profile pictures, and post images. Using the correct dimensions ensures your images look sharp and aren't awkwardly cropped.",
        "sizes": [
            ("Cover Photo", "820 x 312", "2.63:1"),
            ("Profile Picture", "170 x 170", "1:1"),
            ("Post Image", "1200 x 630", "1.91:1"),
            ("Event Cover", "1920 x 1005", "1.91:1"),
            ("Group Cover", "1640 x 856", "1.91:1"),
        ],
        "faq": [
            ("What size should a Facebook cover photo be?", "Facebook cover photos should be 820x312 pixels. On mobile, the sides are cropped, so keep important content centered."),
            ("What size should a Facebook profile picture be?", "Facebook profile pictures should be 170x170 pixels. They're displayed as circles."),
            ("What size should Facebook post images be?", "Facebook post images should be 1200x630 pixels for optimal display in the feed."),
            ("What's the best format for Facebook?", "JPG is recommended for photos, PNG for graphics with text. Facebook compresses uploads, so start with high quality."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a Facebook preset (Cover, Profile, or Post)",
            "Preview the resized image",
            "Download and upload to Facebook",
        ],
        "tips": "Facebook cover photos are cropped differently on mobile vs desktop. Keep important content in the center 640x360 pixels to ensure it's visible on both platforms.",
    },
    "twitter": {
        "name": "X/Twitter",
        "about": "X (formerly Twitter) uses different image sizes for headers, post images, and profile pictures. Using the correct dimensions ensures your images display correctly in the feed and on your profile.",
        "sizes": [
            ("Header", "1500 x 500", "3:1"),
            ("Post Image", "1200 x 675", "16:9"),
            ("Profile Picture", "400 x 400", "1:1"),
        ],
        "faq": [
            ("What size should an X/Twitter header be?", "X/Twitter headers should be 1500x500 pixels (3:1 ratio)."),
            ("What size should X/Twitter post images be?", "X/Twitter post images should be 1200x675 pixels (16:9 ratio) for optimal display."),
            ("What size should an X/Twitter profile picture be?", "X/Twitter profile pictures should be 400x400 pixels. They're displayed as circles."),
            ("What formats does X/Twitter support?", "X/Twitter supports JPG, PNG, GIF, and WebP. JPG is recommended for photos."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select an X/Twitter preset (Header, Post, or Profile)",
            "Preview the resized image",
            "Download and upload to X/Twitter",
        ],
        "tips": "X/Twitter compresses images significantly. For the best quality, upload images at exactly the recommended dimensions. PNG format preserves more detail but has larger file sizes.",
    },
    "pinterest": {
        "name": "Pinterest",
        "about": "Pinterest is a visual platform where image size directly impacts visibility and engagement. Vertical pins (2:3 ratio) perform best as they take up more space in the feed.",
        "sizes": [
            ("Pin", "1000 x 1500", "2:3"),
            ("Profile Picture", "165 x 165", "1:1"),
            ("Board Cover", "222 x 150", "1.48:1"),
        ],
        "faq": [
            ("What size should Pinterest pins be?", "Pinterest pins should be 1000x1500 pixels (2:3 ratio). Vertical pins take up more space and get more engagement."),
            ("What size should a Pinterest profile picture be?", "Pinterest profile pictures should be 165x165 pixels."),
            ("Can I upload square pins?", "Yes, but vertical (2:3) pins perform significantly better as they're more visible in the feed."),
            ("What's the best format for Pinterest?", "JPG is recommended for photos, PNG for graphics with text. Keep files under 20MB."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a Pinterest preset (Pin or Profile)",
            "Preview the resized image",
            "Download and upload to Pinterest",
        ],
        "tips": "Vertical pins (2:3 ratio) get 73% more engagement than square or horizontal pins. Use high-quality images with clear text overlays for the best results.",
    },
    "whatsapp": {
        "name": "WhatsApp",
        "about": "WhatsApp uses square images for profile pictures and vertical images for status updates. Using the correct dimensions ensures your images look sharp and aren't cropped unexpectedly.",
        "sizes": [
            ("Profile Picture", "500 x 500", "1:1"),
            ("Status", "1080 x 1920", "9:16"),
        ],
        "faq": [
            ("What size should a WhatsApp profile picture be?", "WhatsApp profile pictures should be 500x500 pixels. They're displayed as circles."),
            ("What size should WhatsApp status be?", "WhatsApp status images should be 1080x1920 pixels (9:16 ratio)."),
            ("What formats does WhatsApp support?", "WhatsApp supports JPG and PNG for images. JPG is recommended for smaller file sizes."),
            ("Will WhatsApp compress my images?", "Yes, WhatsApp compresses images by default. Send as 'Document' to preserve quality."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a WhatsApp preset (Profile or Status)",
            "Preview the resized image",
            "Download and upload to WhatsApp",
        ],
        "tips": "WhatsApp compresses images heavily when sending as photos. To preserve quality, send images as 'Document' instead. For status updates, use vertical (9:16) images for the best display.",
    },
    "snapchat": {
        "name": "Snapchat",
        "about": "Snapchat uses square images for icons and vertical images for stories. Using the correct dimensions ensures your content looks great on the platform.",
        "sizes": [
            ("Icon", "320 x 320", "1:1"),
            ("Story", "1080 x 1920", "9:16"),
        ],
        "faq": [
            ("What size should a Snapchat icon be?", "Snapchat icons should be 320x320 pixels."),
            ("What size should Snapchat stories be?", "Snapchat stories should be 1080x1920 pixels (9:16 ratio)."),
            ("What formats does Snapchat support?", "Snapchat supports JPG and PNG for images."),
            ("Can I upload horizontal images?", "You can, but vertical (9:16) is strongly recommended for stories."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Select a Snapchat preset (Icon or Story)",
            "Preview the resized image",
            "Download and upload to Snapchat",
        ],
        "tips": "Snapchat is a vertical-first platform. Always use 9:16 ratio for stories. For icons, keep designs simple and recognizable at small sizes.",
    },
    "generic": {
        "name": "Generic",
        "about": "Our image resizer supports any custom dimensions. Whether you need images for websites, documents, presentations, or any other purpose, you can resize to any size you need.",
        "sizes": [],
        "faq": [
            ("What image formats are supported?", "We support PNG, JPG, JPEG, and WebP formats. Output can be PNG or JPG."),
            ("Is there a file size limit?", "There's no strict limit, but very large images (over 50MB) may be slower to process."),
            ("Will resizing reduce quality?", "Reducing size generally maintains quality. Enlarging images may cause some blurriness."),
            ("Is my image uploaded to a server?", "No. All processing happens locally in your browser. Your images never leave your device."),
        ],
        "how_to": [
            "Upload your image to the tool above",
            "Enter your desired width and height",
            "Toggle aspect ratio lock if needed",
            "Preview and download the resized image",
        ],
        "tips": "When resizing, it's better to reduce dimensions than to enlarge them. Enlarging images can cause blurriness and pixelation. Always keep a copy of the original image.",
    },
    # NEW enrichment types for long-tail pages（2026-06-14）
    "social-media-dimensions": {
        "name": "Social Media",
        "about": "Every social media platform has different image size requirements. Using the correct dimensions ensures your photos, banners, and profile pictures look professional and aren't awkwardly cropped. This guide covers all major platforms with the latest 2026 dimensions.",
        "sizes": [
            ("Instagram Post (Square)", "1080 x 1080", "1:1"),
            ("Instagram Story / Reel", "1080 x 1920", "9:16"),
            ("Facebook Cover", "820 x 312", "2.63:1"),
            ("Facebook Post", "1200 x 630", "1.91:1"),
            ("LinkedIn Banner", "1584 x 396", "4:1"),
            ("LinkedIn Post", "1200 x 627", "1.91:1"),
            ("X/Twitter Header", "1500 x 500", "3:1"),
            ("X/Twitter Post", "1200 x 675", "16:9"),
            ("YouTube Thumbnail", "1280 x 720", "16:9"),
            ("YouTube Banner", "2560 x 1440", "16:9"),
            ("TikTok Video", "1080 x 1920", "9:16"),
            ("Pinterest Pin", "1000 x 1500", "2:3"),
            ("Discord Avatar", "512 x 512", "1:1"),
            ("Discord Banner", "680 x 240", "2.83:1"),
        ],
        "faq": [
            ("What are the most common social media image sizes?", "The most common sizes are 1080x1080 (Instagram post), 1080x1920 (Stories/Reels/TikTok), 1200x630 (Facebook/LinkedIn posts), and 1280x720 (YouTube thumbnails)."),
            ("Do image dimensions affect engagement?", "Yes. Correctly sized images look professional and get more likes, shares, and comments. Cropped or stretched images reduce trust and engagement."),
            ("What happens if I upload the wrong image size?", "Social media platforms will automatically crop or resize your image, which may cut off important parts or reduce quality. Always resize to the recommended dimensions first."),
            ("Are these dimensions updated for 2026?", "Yes. All dimensions in this guide are verified for 2026. Social media platforms occasionally update their requirements, and we keep this guide current."),
        ],
        "how_to": [
            "Find your platform in the size table above",
            "Use the resize tool to set the exact dimensions",
            "Preview and adjust if needed",
            "Download and upload to your social platform",
        ],
        "tips": "Portrait/vertical images (9:16) take up more screen space on mobile and tend to get more engagement on Instagram, TikTok, and Snapchat. For LinkedIn and Facebook, horizontal (1.91:1) is the standard for feed posts.",
    },
    "printing": {
        "name": "Printing",
        "about": "Resizing images for printing is different from resizing for screens. Print requires higher DPI (dots per inch) — typically 300 DPI — to look sharp. Screen images at 72 DPI will look pixelated when printed. Use this tool to resize images to print-ready dimensions in inches, centimeters, or millimeters.",
        "sizes": [
            ("4×6 Photo Print", "1200 x 1800", "300 DPI"),
            ("5×7 Photo Print", "1500 x 2100", "300 DPI"),
            ("8×10 Photo Print", "2400 x 3000", "300 DPI"),
            ("A4 Print", "2480 x 3508", "300 DPI"),
            ("Letter Size", "2550 x 3300", "300 DPI"),
            ("Poster 18×24", "5400 x 7200", "300 DPI"),
        ],
        "faq": [
            ("What DPI should I use for printing?", "300 DPI is the standard for high-quality prints. For large posters viewed from a distance, 150 DPI can be acceptable. Never print at 72 DPI (screen resolution)."),
            ("How do I calculate print dimensions in pixels?", "Multiply inches by DPI. For example, a 4×6 inch photo at 300 DPI = 1200×1800 pixels."),
            ("What's the difference between screen and print resolution?", "Screen images use 72-96 DPI and look fine on monitors. Print requires 300 DPI for sharp output. Always resize to 300 DPI before printing."),
            ("Does resizing for print reduce quality?", "Enlarging an image for print can cause quality loss. Start with the highest resolution source image possible."),
        ],
        "how_to": [
            "Upload your image above",
            "Enter target dimensions in inches/cm (convert to pixels at 300 DPI)",
            "Check the preview for sharpness",
            "Download and send to your printer",
        ],
        "tips": "For the best print quality, start with images at least 300 DPI at the desired print size. If your image is too small, you may need to scan at higher resolution or use AI upscaling tools before resizing.",
    },
    "resolution": {
        "name": "Resolution",
        "about": "Image resolution determines how sharp and detailed your image appears. Changing resolution (DPI/PPI) affects print quality without changing the pixel dimensions. You can also change the total pixel count to reduce file size for web use.",
        "sizes": [
            ("Web / Screen", "72 PPI", "Standard"),
            ("HD Display", "1920 x 1080", "1080p"),
            ("4K Display", "3840 x 2160", "4K"),
            ("Print Standard", "300 PPI", "High quality"),
        ],
        "faq": [
            ("What's the difference between DPI and PPI?", "DPI (Dots Per Inch) is for printing; PPI (Pixels Per Inch) is for screens. They're often used interchangeably. Higher DPI/PPI = sharper image."),
            ("Can I increase resolution without losing quality?", "Reducing resolution keeps quality intact. Increasing resolution (upscaling) often causes blurriness. For significant upscaling, use AI-powered tools."),
            ("What resolution should I use for web?", "72-96 PPI is standard for web. For Retina/HiDPI displays, use 2x the dimensions (e.g., 2000px wide for a 1000px container)."),
            ("Does changing resolution change file size?", "Changing PPI metadata doesn't change file size. Changing actual pixel dimensions does change file size."),
        ],
        "how_to": [
            "Upload your image above",
            "Enter new dimensions or DPI value",
            "Preview to check quality",
            "Download the resolution-adjusted image",
        ],
        "tips": "For sharp Retina display images, export at 2x your target display size. A 1000px-wide image will look crisp on Retina screens when exported at 2000px.",
    },
    "image-size-guide": {
        "name": "Image Size Guide",
        "about": "This is the complete image size reference for 2026. Whether you're designing for social media, websites, email, or print — you'll find every dimension you need in one place. Bookmark this page as your go-to image size cheat sheet.",
        "sizes": [
            ("Instagram Post", "1080 x 1080 (square) / 1080 x 1350 (portrait)", "1:1 / 4:5"),
            ("Instagram Story", "1080 x 1920", "9:16"),
            ("Facebook Cover", "820 x 312", "2.63:1"),
            ("Facebook Profile", "170 x 170", "1:1"),
            ("LinkedIn Banner", "1584 x 396", "4:1"),
            ("LinkedIn Profile", "400 x 400", "1:1"),
            ("X/Twitter Header", "1500 x 500", "3:1"),
            ("YouTube Thumbnail", "1280 x 720", "16:9"),
            ("YouTube Banner", "2560 x 1440", "16:9"),
            ("TikTok Video", "1080 x 1920", "9:16"),
            ("Pinterest Pin", "1000 x 1500", "2:3"),
            ("Discord Avatar", "512 x 512", "1:1"),
            ("Discord Banner", "680 x 240", "2.83:1"),
            ("Email Header", "600 x 200", "3:1"),
            ("Website Hero Banner", "1920 x 600", "3.2:1"),
            ("Blog Featured Image", "1200 x 630", "1.91:1"),
        ],
        "faq": [
            ("Why do image sizes matter?", "Wrong image sizes get cropped, stretched, or compressed by platforms — making your content look unprofessional. Correct dimensions ensure pixel-perfect display everywhere."),
            ("How often do social media image sizes change?", "Major platforms update their dimensions every 1-3 years. We keep this guide updated with the latest 2026 requirements."),
            ("What's the best image format for social media?", "JPG for photos, PNG for graphics with text/logos. WebP is gaining support and offers better compression. This guide lists recommended formats per platform."),
            ("Can I use the same image size for all platforms?", "No — each platform has unique dimensions. The tool on this page lets you select platform presets to quickly resize one image for multiple platforms."),
        ],
        "how_to": [
            "Find your platform in the size table",
            "Note the recommended dimensions",
            "Use the resize tool with those dimensions",
            "Download the perfectly sized image",
        ],
        "tips": "Bookmark this page as your image size reference. When creating content, start with the largest size needed and resize down — this preserves the most quality.",
    },
}

# Generic enrichment for pages without specific platform data
GENERIC_ENRICHMENT = {
    "about": "Resize images online for free. Our browser-based tool supports any dimensions and format. No upload required — your images stay private on your device.",
    "faq": [
        ("How do I resize an image?", "Upload your image, enter the desired width and height, and click download. It's that simple."),
        ("Is this tool free?", "Yes, completely free. No signup, no watermarks, no limits."),
        ("Is my image uploaded to a server?", "No. All processing happens locally in your browser. Your images never leave your device."),
        ("What formats are supported?", "PNG, JPG, JPEG, and WebP are supported for both input and output."),
    ],
    "how_to": [
        "Upload or drag your image into the tool",
        "Enter the desired width and height",
        "Toggle aspect ratio lock if needed",
        "Download the resized image",
    ],
    "tips": "For the best quality, resize images down rather than up. Enlarging images can cause blurriness. Always keep a copy of your original image.",
}

def get_content(s):
    """Get platform-specific or generic content for a page."""
    platform = s.get("platform", "generic")
    if platform in PLATFORM_DATA:
        return PLATFORM_DATA[platform]
    return GENERIC_ENRICHMENT

# ═══ Page Template ═════════════════════════════════

def build_scene_page(s):
    content = get_content(s)
    title = s["title"]
    desc = s["desc"]
    slug = s["slug"]
    platform = s.get("platform", "generic")

    # Build FAQ HTML
    faq_html = ""
    for q, a in content.get("faq", []):
        faq_html += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'

    # Build FAQ Schema
    faq_schema = []
    for q, a in content.get("faq", []):
        faq_schema.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
    faq_schema_json = ",".join(faq_schema)

    # Build size table if available
    size_table = ""
    if content.get("sizes"):
        rows = ""
        for name, dims, ratio in content["sizes"]:
            rows += f"<tr><td>{name}</td><td>{dims}</td><td>{ratio}</td></tr>"
        size_table = f"""
        <h2>{content['name']} Image Sizes</h2>
        <table class="size-table">
            <thead><tr><th>Type</th><th>Dimensions</th><th>Ratio</th></tr></thead>
            <tbody>{rows}</tbody>
        </table>"""

    # Build how-to steps
    how_to_html = "".join(f"<p>Step {i+1}: {step}</p>" for i, step in enumerate(content.get("how_to", [])))

    # Build related links
    related = random.sample([s2 for s2 in ALL_SCENARIOS if s2["slug"] != slug], min(6, len(ALL_SCENARIOS)-1))
    related_html = "".join(f'<li><a href="/{r["slug"]}/">{r["title"].split("—")[0].strip()}</a></li>' for r in related)

    # Preset selector options
    preset_options = ""
    for pid, p in PRESETS.items():
        preset_options += f'<option value="{pid}">{p["name"]} ({p["width"]}x{p["height"]})</option>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="msvalidate.01" content="1F14EEA4478F7A176F2E0451992C984C">
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://{DOMAIN}/{slug}/">
    <link rel="canonical" href="https://{DOMAIN}/{slug}/">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-Z9NW1GSG04");</script>
    <style>
        :root{{--primary:#4F46E5;--primary-dark:#4338CA;--bg:#FAFAFA;--card-bg:#FFFFFF;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:24px;--radius-sm:12px}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:960px;margin:0 auto;padding:0 24px}}
header{{background:#1E293B;color:#F1F5F9;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
header .container{{display:flex;justify-content:space-between;align-items:center}}
header nav{{display:flex;gap:24px}}header nav a{{color:#94A3B8;text-decoration:none;font-size:.9rem;font-weight:500}}header nav a:hover{{color:#fff}}
.hero{{padding:60px 0 40px;text-align:center}}
.hero h1{{font-size:2.5rem;font-weight:800;margin-bottom:16px;line-height:1.2}}
.hero p{{color:var(--text-secondary);font-size:1.1rem;max-width:600px;margin:0 auto}}
.tool-area{{max-width:700px;margin:0 auto 40px;padding:0 24px}}
.drop-zone{{border:2px dashed var(--border);border-radius:32px;padding:40px 20px;text-align:center;cursor:pointer;background:var(--card-bg);transition:all .2s}}
.drop-zone:hover{{border-color:var(--primary);background:#F5F3FF}}
.btn-row{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:24px}}
.btn{{padding:14px 28px;border:none;border-radius:var(--radius-sm);font-size:1rem;font-weight:600;cursor:pointer;font-family:inherit;transition:all .15s}}.btn:active{{transform:scale(.97)}}
.btn-primary{{background:var(--primary);color:#fff;height:56px}}.btn-primary:hover{{background:var(--primary-dark)}}
.btn-secondary{{background:var(--card-bg);color:var(--text);border:1px solid var(--border)}}
.controls{{background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-top:20px}}
.control-row{{display:flex;gap:16px;align-items:center;margin-bottom:16px;flex-wrap:wrap}}
.control-row label{{font-weight:600;font-size:.9rem;min-width:80px}}
.control-row input{{width:120px;padding:12px;border:1px solid var(--border);border-radius:var(--radius-sm);font-size:1rem;font-family:inherit}}
.control-row select{{flex:1;padding:12px;border:1px solid var(--border);border-radius:var(--radius-sm);font-size:1rem;font-family:inherit}}
.toggle{{display:flex;align-items:center;gap:8px;cursor:pointer}}
.toggle input{{width:18px;height:18px}}
.preview-area{{display:none;margin-top:20px}}
.preview-area img{{max-width:100%;border-radius:var(--radius);border:1px solid var(--border)}}
.stats{{background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius-sm);padding:16px;margin:16px 0;font-size:.9rem}}
.section{{padding:40px 0}}.section h2{{font-size:1.5rem;margin-bottom:20px}}
.size-table{{width:100%;border-collapse:collapse;margin:20px 0}}
.size-table th,.size-table td{{padding:12px 16px;border:1px solid var(--border);text-align:left;font-size:.9rem}}
.size-table th{{background:var(--card-bg);font-weight:600}}
.faq-section{{padding:40px 0;text-align:left}}.faq-section h2{{font-size:1.5rem;margin-bottom:24px;text-align:center}}
.faq-item{{margin-bottom:20px;background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);padding:20px}}
.faq-item h3{{font-size:1rem;margin-bottom:8px;color:var(--primary)}}
.faq-item p{{color:var(--text-secondary);font-size:.9rem}}
.cross-site{{max-width:700px;margin:0 auto 40px;padding:20px;background:#F5F0FF;border-left:3px solid var(--primary);border-radius:0 var(--radius-sm) var(--radius-sm) 0}}
.cross-site strong{{color:var(--primary)}}.cross-site a{{color:var(--primary);font-weight:600}}
.related-tools{{background:var(--bg);border-top:1px solid var(--border);padding:40px 0}}
.related-tools ul{{list-style:none;display:grid;grid-template-columns:repeat(2,1fr);gap:12px;max-width:600px;margin:0 auto}}
.related-tools a{{color:var(--primary);text-decoration:none;font-weight:500;padding:12px 16px;display:block;background:var(--card-bg);border-radius:var(--radius-sm);border:1px solid var(--border);transition:all .15s}}
.related-tools a:hover{{border-color:var(--primary);box-shadow:0 4px 12px rgba(79,70,229,.1)}}
footer{{background:#1E293B;color:#94A3B8;padding:32px 0;text-align:center;font-size:.85rem}}
footer a{{color:#CBD5E1;text-decoration:none}}
.breadcrumb{{font-size:.85rem;color:var(--text-secondary);padding:16px 0;max-width:960px;margin:0 auto}}
.breadcrumb a{{color:var(--primary);text-decoration:none}}
@media(max-width:640px){{.hero h1{{font-size:1.8rem}}.control-row{{flex-direction:column}}.related-tools ul{{grid-template-columns:1fr}}}}
    </style>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"WebApplication","name":"{title}","url":"https://{DOMAIN}/{slug}/","description":"{desc}","applicationCategory":"MultimediaApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_schema_json}]}}
    </script>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://{DOMAIN}/"}},{{"@type":"ListItem","position":2,"name":"{title.split("—")[0].strip()}","item":"https://{DOMAIN}/{slug}/"}}]}}
    </script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"ResizeNow","url":"https://resizenow.net","description":"Free online image resizer","applicationCategory":"MultimediaApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script></head>
<body>
    <header>
        <div class="container">
            <a href="/" style="font-size:1.2rem;font-weight:700;color:#F1F5F9;text-decoration:none">Resize<span style="color:#818CF8">Now</span></a>
            <nav>
                <a href="/">Home</a>
                <a href="/resize-image-for-instagram/">Instagram</a>
                <a href="/resize-image-for-discord/">Discord</a>
                <a href="#faq">FAQ</a>
            </nav>
        </div>
    </header>
    <main>
        <div class="container">
            <div class="breadcrumb"><a href="/">Home</a> / {title.split("—")[0].strip()}</div>
        </div>
        <section class="hero">
            <h1>{title.split("—")[0].strip()}</h1>
            <p>{desc}</p>
        </section>
        <section class="tool-area">
            <div class="drop-zone" id="dropZone">
                <p style="font-size:2rem;margin-bottom:8px">📁</p>
                <p style="font-weight:600;margin-bottom:4px">Drop image here or click to upload</p>
                <p style="color:var(--text-secondary);font-size:.85rem">Supports PNG, JPEG, WebP</p>
                <input type="file" id="fileInput" accept="image/*" style="display:none">
            </div>
            <div class="controls" id="controls" style="display:none">
                <div class="control-row">
                    <label>Preset:</label>
                    <select id="presetSelect">
                        <option value="">Custom Size</option>
                        {preset_options}
                    </select>
                </div>
                <div class="control-row">
                    <label>Width:</label>
                    <input type="number" id="widthInput" placeholder="Width (px)">
                    <label>Height:</label>
                    <input type="number" id="heightInput" placeholder="Height (px)">
                    <div class="toggle">
                        <input type="checkbox" id="lockRatio" checked>
                        <label for="lockRatio" style="font-size:.85rem;min-width:auto">Lock Ratio</label>
                    </div>
                </div>
                <div class="btn-row">
                    <button class="btn btn-primary" id="resizeBtn">Resize Image</button>
                    <button class="btn btn-secondary" id="resetBtn">🔄 Start Over</button>
                </div>
            </div>
            <div class="preview-area" id="previewArea">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
                    <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Original</p><img id="originalPreview"></div>
                    <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Resized</p><img id="resizedPreview"></div>
                </div>
                <div class="stats" id="stats"></div>
                <div class="btn-row">
                    <button class="btn btn-primary" id="downloadPng">⬇ Download PNG</button>
                    <button class="btn btn-secondary" id="downloadJpg">⬇ Download JPG</button>
                </div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <h2>About {content.get('name', '')} Image Sizes</h2>
                <p>{content.get('about', '')}</p>
                {size_table}
                <h2>How to Resize</h2>
                {how_to_html}
                <h2>Tips</h2>
                <p>{content.get('tips', '')}</p>
            </div>
        </section>
        <div class="cross-site">
            <strong>Pro Tip</strong> — Done resizing? Optimize file size with our <a href="https://compressnow.net">file optimizer</a>. Build a resume? <a href="https://cvbuild-ai.com">CVBuild-AI</a>. Write emails? <a href="https://messagegen-ai.com">MessageGen-AI</a>. Adjust tone? <a href="https://tonemodifier.com">ToneModifier</a>.
        </div>
        <section class="faq-section" id="faq">
            <div class="container">
                <h2>Frequently Asked Questions</h2>
                {faq_html}
            </div>
        </section>
        <section class="related-tools">
            <div class="container">
                <h2 style="text-align:center;margin-bottom:20px">Related Tools</h2>
                <ul>{related_html}</ul>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 ResizeNow. All rights reserved. | <a href="/">Home</a> | <a href="#faq">FAQ</a></p>
            <p style="margin-top:8px">All processing happens locally in your browser. Your images are never uploaded.</p>
        </div>
    </footer>
    <script>
    const PRESETS = {json.dumps(PRESETS)};
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const controls = document.getElementById('controls');
    const presetSelect = document.getElementById('presetSelect');
    const widthInput = document.getElementById('widthInput');
    const heightInput = document.getElementById('heightInput');
    const lockRatio = document.getElementById('lockRatio');
    const resizeBtn = document.getElementById('resizeBtn');
    const resetBtn = document.getElementById('resetBtn');
    const previewArea = document.getElementById('previewArea');
    const originalPreview = document.getElementById('originalPreview');
    const resizedPreview = document.getElementById('resizedPreview');
    const stats = document.getElementById('stats');
    const downloadPng = document.getElementById('downloadPng');
    const downloadJpg = document.getElementById('downloadJpg');

    let originalImage = null;
    let originalWidth = 0;
    let originalHeight = 0;
    let resizedCanvas = null;

    dropZone.addEventListener('click', () => fileInput.click());
    dropZone.addEventListener('dragover', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--primary)'; }});
    dropZone.addEventListener('dragleave', () => {{ dropZone.style.borderColor = 'var(--border)'; }});
    dropZone.addEventListener('drop', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--border)'; if(e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]); }});
    fileInput.addEventListener('change', () => {{ if(fileInput.files.length) handleFile(fileInput.files[0]); }});
    presetSelect.addEventListener('change', () => {{ const p = PRESETS[presetSelect.value]; if(p) {{ widthInput.value = p.width; heightInput.value = p.height; }} }});
    widthInput.addEventListener('input', () => {{ if(lockRatio.checked && originalWidth) {{ heightInput.value = Math.round(widthInput.value * originalHeight / originalWidth); }} }});
    heightInput.addEventListener('input', () => {{ if(lockRatio.checked && originalHeight) {{ widthInput.value = Math.round(heightInput.value * originalWidth / originalHeight); }} }});
    resizeBtn.addEventListener('click', resizeImage);
    resetBtn.addEventListener('click', resetAll);
    downloadPng.addEventListener('click', () => download('png'));
    downloadJpg.addEventListener('click', () => download('jpeg'));

    function handleFile(file) {{ if(!file.type.match(/^image\\/(png|jpeg|webp)$/)) return; const reader = new FileReader(); reader.onload = e => {{ const img = new Image(); img.onload = () => {{ originalImage = img; originalWidth = img.width; originalHeight = img.height; originalPreview.src = e.target.result; widthInput.value = img.width; heightInput.value = img.height; dropZone.style.display = 'none'; controls.style.display = 'block'; }}; img.src = e.target.result; }}; reader.readAsDataURL(file); }}

    function resizeImage() {{ if(!originalImage) return; const w = parseInt(widthInput.value); const h = parseInt(heightInput.value); if(!w || !h) return; const canvas = document.createElement('canvas'); canvas.width = w; canvas.height = h; const ctx = canvas.getContext('2d'); ctx.drawImage(originalImage, 0, 0, w, h); resizedCanvas = canvas; resizedPreview.src = canvas.toDataURL(); const origSize = fileInput.files[0].size; const newSize = Math.round(canvas.toDataURL().length * 0.75); stats.innerHTML = '<div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px"><div><strong>Original:</strong> ' + originalWidth + ' x ' + originalHeight + '</div><div><strong>Resized:</strong> ' + w + ' x ' + h + '</div><div><strong>Original Size:</strong> ' + formatSize(origSize) + '</div><div><strong>New Size:</strong> ~' + formatSize(newSize) + '</div></div>'; previewArea.style.display = 'block'; }}

    function download(format) {{ if(!resizedCanvas) return; const link = document.createElement('a'); link.download = 'resized-' + fileInput.files[0].name.replace(/\\.[^.]+$/, '') + '.' + (format === 'png' ? 'png' : 'jpg'); link.href = resizedCanvas.toDataURL('image/' + format, 0.92); link.click(); }}

    function resetAll() {{ originalImage = null; originalWidth = 0; originalHeight = 0; resizedCanvas = null; fileInput.value = ''; dropZone.style.display = 'block'; controls.style.display = 'none'; previewArea.style.display = 'none'; }}

    function formatSize(bytes) {{ if(bytes < 1024) return bytes + ' B'; if(bytes < 1048576) return (bytes/1024).toFixed(1) + ' KB'; return (bytes/1048576).toFixed(2) + ' MB'; }}
    </script>
</body>
</html>"""


def build_home():
    # Platform cards
    platform_cards = ""
    for slug, name in [
        ("resize-image-for-instagram", "Instagram"),
        ("resize-image-for-tiktok", "TikTok"),
        ("resize-image-for-youtube", "YouTube"),
        ("resize-image-for-discord", "Discord"),
        ("resize-image-for-linkedin", "LinkedIn"),
        ("resize-image-for-facebook", "Facebook"),
        ("resize-image-for-twitter", "X/Twitter"),
        ("resize-image-for-pinterest", "Pinterest"),
        ("resize-image-for-whatsapp", "WhatsApp"),
    ]:
        platform_cards += f'<a href="/{slug}/" class="card">{name}</a>'

    # Popular preset cards
    preset_cards = ""
    for pid in ["instagram-story", "tiktok-video", "youtube-thumbnail", "discord-avatar", "linkedin-banner", "facebook-cover"]:
        p = PRESETS[pid]
        preset_cards += f'<a href="/resize-image-for-{p["platform"].lower()}/" class="card">{p["name"]}<br><small style="color:var(--text-secondary)">{p["width"]}x{p["height"]}</small></a>'

    # Preset options for homepage
    preset_options = ""
    for pid, p in PRESETS.items():
        preset_options += f'<option value="{pid}">{p["name"]} ({p["width"]}x{p["height"]})</option>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="msvalidate.01" content="1F14EEA4478F7A176F2E0451992C984C">
    <meta name="description" content="Resize images for Instagram, TikTok, YouTube, Discord, LinkedIn and more. Free online image resizer with platform presets. No signup required.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://{DOMAIN}/">
    <meta property="og:title" content="Resize Images for Any Platform Instantly | ResizeNow">
    <meta property="og:description" content="Resize images for Instagram, TikTok, YouTube, Discord, LinkedIn and more. Free, no signup.">
    <meta property="og:url" content="https://{DOMAIN}/">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <title>Resize Images for Any Platform Instantly | ResizeNow</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"ResizeNow","url":"https://{DOMAIN}","description":"Free online image resizer for social media platforms."}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebApplication","name":"ResizeNow","url":"https://{DOMAIN}","applicationCategory":"MultimediaApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"How does ResizeNow work?","acceptedAnswer":{{"@type":"Answer","text":"Upload your image, choose a platform preset or enter custom dimensions, and download the resized image. Everything happens in your browser — no upload to server."}}}},{{"@type":"Question","name":"Is ResizeNow free?","acceptedAnswer":{{"@type":"Answer","text":"Yes, completely free. No signup, no watermarks, no limits. Resize as many images as you need."}}}},{{"@type":"Question","name":"What platforms are supported?","acceptedAnswer":{{"@type":"Answer","text":"Instagram, TikTok, YouTube, Discord, LinkedIn, Facebook, X/Twitter, Pinterest, WhatsApp, Snapchat, and custom sizes."}}}},{{"@type":"Question","name":"Is my image uploaded to a server?","acceptedAnswer":{{"@type":"Answer","text":"No. All processing happens locally in your browser. Your images never leave your device."}}}}]}}</script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z9NW1GSG04"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-Z9NW1GSG04");</script>
    <style>
        :root{{--primary:#4F46E5;--primary-dark:#4338CA;--bg:#FAFAFA;--card-bg:#FFFFFF;--text:#1E293B;--text-secondary:#64748B;--border:#E2E8F0;--radius:24px;--radius-sm:12px}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.container{{max-width:960px;margin:0 auto;padding:0 24px}}
header{{background:#1E293B;color:#F1F5F9;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
header .container{{display:flex;justify-content:space-between;align-items:center}}
header nav{{display:flex;gap:24px}}header nav a{{color:#94A3B8;text-decoration:none;font-size:.9rem;font-weight:500}}header nav a:hover{{color:#fff}}
.hero{{padding:80px 0 40px;text-align:center}}
.hero h1{{font-size:2.8rem;font-weight:800;margin-bottom:16px;line-height:1.2}}
.hero p{{color:var(--text-secondary);font-size:1.1rem;max-width:600px;margin:0 auto 24px}}
.trust{{display:flex;justify-content:center;gap:24px;flex-wrap:wrap;color:var(--text-secondary);font-size:.9rem;margin-top:24px}}
.tool-area{{max-width:700px;margin:0 auto 40px;padding:0 24px}}
.drop-zone{{border:2px dashed var(--border);border-radius:32px;padding:60px 20px;text-align:center;cursor:pointer;background:var(--card-bg);transition:all .2s}}
.drop-zone:hover{{border-color:var(--primary);background:#F5F3FF;transform:scale(1.02)}}
.section{{padding:40px 0}}.section h2{{font-size:1.5rem;margin-bottom:20px;text-align:center}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:700px;margin:0 auto}}
@media(max-width:640px){{.grid{{grid-template-columns:repeat(2,1fr)}}.hero h1{{font-size:2rem}}}}
.card{{padding:20px;background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);text-align:center;text-decoration:none;color:var(--text);font-weight:600;font-size:.95rem;transition:all .15s}}
.card:hover{{border-color:var(--primary);box-shadow:0 8px 24px rgba(79,70,229,.1);transform:scale(1.02)}}
.card small{{font-weight:400}}
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:700px;margin:0 auto;text-align:center}}
.step-num{{width:48px;height:48px;background:var(--primary);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.2rem;margin:0 auto 12px}}
.faq-section{{padding:40px 0;text-align:left}}.faq-section h2{{font-size:1.5rem;margin-bottom:24px;text-align:center}}
.faq-item{{margin-bottom:16px;background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);padding:20px}}
.faq-item h3{{font-size:1rem;margin-bottom:8px;color:var(--primary)}}
.faq-item p{{color:var(--text-secondary);font-size:.9rem}}
.cross-site{{max-width:700px;margin:0 auto 40px;padding:20px;background:#F5F0FF;border-left:3px solid var(--primary);border-radius:0 var(--radius-sm) var(--radius-sm) 0}}
.cross-site strong{{color:var(--primary)}}.cross-site a{{color:var(--primary);font-weight:600}}
footer{{background:#1E293B;color:#94A3B8;padding:32px 0;text-align:center;font-size:.85rem}}
footer a{{color:#CBD5E1;text-decoration:none}}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <a href="/" style="font-size:1.2rem;font-weight:700;color:#F1F5F9;text-decoration:none">Resize<span style="color:#818CF8">Now</span></a>
            <nav>
                <a href="/">Home</a>
                <a href="/resize-image-for-instagram/">Instagram</a>
                <a href="/resize-image-for-discord/">Discord</a>
                <a href="#faq">FAQ</a>
            </nav>
        </div>
    </header>
    <main>
        <section class="hero">
            <div class="container">
                <h1>Resize Images for Any Platform</h1>
                <p>Resize images for Instagram, TikTok, YouTube, Discord, LinkedIn and more. Free, no signup required.</p>
                <div class="trust">
                    <span>✓ Free Forever</span>
                    <span>✓ No Signup</span>
                    <span>✓ 10+ Platforms</span>
                    <span>✓ 100% Private</span>
                </div>
                <p style="color:var(--text-secondary);font-size:.85rem;margin-top:16px">Trusted by thousands of creators, marketers, and designers since 2025. All processing happens locally — your images never leave your device.</p>
            </div>
        </section>
        <section class="tool-area">
            <div class="drop-zone" id="dropZone">
                <p style="font-size:2.5rem;margin-bottom:12px">📁</p>
                <p style="font-weight:700;font-size:1.1rem;margin-bottom:4px">Drop image here or click to upload</p>
                <p style="color:var(--text-secondary);font-size:.9rem">Supports PNG, JPEG, WebP</p>
                <input type="file" id="fileInput" accept="image/*" style="display:none">
            </div>
            <div id="toolControls" style="display:none">
                <div style="background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-top:20px">
                    <div style="display:flex;gap:16px;align-items:center;margin-bottom:16px;flex-wrap:wrap">
                        <label style="font-weight:600;font-size:.9rem;min-width:80px">Preset:</label>
                        <select id="presetSelect" style="flex:1;padding:12px;border:1px solid var(--border);border-radius:var(--radius-sm);font-size:1rem;font-family:inherit">
                            <option value="">Custom Size</option>
                            {preset_options}
                        </select>
                    </div>
                    <div style="display:flex;gap:16px;align-items:center;margin-bottom:16px;flex-wrap:wrap">
                        <label style="font-weight:600;font-size:.9rem;min-width:80px">Width:</label>
                        <input type="number" id="widthInput" placeholder="Width (px)" style="width:120px;padding:12px;border:1px solid var(--border);border-radius:var(--radius-sm);font-size:1rem">
                        <label style="font-weight:600;font-size:.9rem;min-width:80px">Height:</label>
                        <input type="number" id="heightInput" placeholder="Height (px)" style="width:120px;padding:12px;border:1px solid var(--border);border-radius:var(--radius-sm);font-size:1rem">
                        <div style="display:flex;align-items:center;gap:8px">
                            <input type="checkbox" id="lockRatio" checked style="width:18px;height:18px">
                            <label for="lockRatio" style="font-size:.85rem">Lock Ratio</label>
                        </div>
                    </div>
                    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
                        <button id="resizeBtn" style="padding:14px 28px;background:var(--primary);color:#fff;border:none;border-radius:var(--radius-sm);font-size:1rem;font-weight:600;cursor:pointer;height:56px;font-family:inherit">Resize Image</button>
                        <button id="resetBtn" style="padding:14px 28px;background:var(--card-bg);color:var(--text);border:1px solid var(--border);border-radius:var(--radius-sm);font-size:1rem;font-weight:600;cursor:pointer;font-family:inherit">🔄 Start Over</button>
                    </div>
                </div>
                <div id="previewArea" style="display:none;margin-top:20px">
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
                        <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Original</p><img id="originalPreview" style="max-width:100%;border-radius:var(--radius);border:1px solid var(--border)"></div>
                        <div style="text-align:center"><p style="font-size:.8rem;color:var(--text-secondary);margin-bottom:8px">Resized</p><img id="resizedPreview" style="max-width:100%;border-radius:var(--radius);border:1px solid var(--border)"></div>
                    </div>
                    <div id="stats" style="background:var(--card-bg);border:1px solid var(--border);border-radius:var(--radius-sm);padding:16px;margin:16px 0;font-size:.9rem"></div>
                    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
                        <button id="downloadPng" style="padding:14px 28px;background:var(--primary);color:#fff;border:none;border-radius:var(--radius-sm);font-size:1rem;font-weight:600;cursor:pointer;height:56px;font-family:inherit">⬇ Download PNG</button>
                        <button id="downloadJpg" style="padding:14px 28px;background:var(--card-bg);color:var(--text);border:1px solid var(--border);border-radius:var(--radius-sm);font-size:1rem;font-weight:600;cursor:pointer;font-family:inherit">⬇ Download JPG</button>
                    </div>
                </div>
            </div>
        </section>
        <div class="cross-site">
            <strong>Pro Tip</strong> — Done resizing? Optimize file size with our <a href="https://compressnow.net">file optimizer</a>. Build a resume? <a href="https://cvbuild-ai.com">CVBuild-AI</a>. Write emails? <a href="https://messagegen-ai.com">MessageGen-AI</a>. Adjust tone? <a href="https://tonemodifier.com">ToneModifier</a>.
        </div>
        <section class="section">
            <h2>Resize by Platform</h2>
            <div class="grid">{platform_cards}</div>
        </section>
        <section class="section">
            <h2>Popular Sizes</h2>
            <div class="grid">{preset_cards}</div>
        </section>
        <section class="section">
            <h2>How It Works</h2>
            <div class="steps">
                <div><div class="step-num">1</div><h3 style="font-size:1rem;margin-bottom:8px">Upload</h3><p style="color:var(--text-secondary);font-size:.9rem">Drop your image or click to upload</p></div>
                <div><div class="step-num">2</div><h3 style="font-size:1rem;margin-bottom:8px">Choose Size</h3><p style="color:var(--text-secondary);font-size:.9rem">Select a platform preset or enter custom dimensions</p></div>
                <div><div class="step-num">3</div><h3 style="font-size:1rem;margin-bottom:8px">Download</h3><p style="color:var(--text-secondary);font-size:.9rem">Preview and download your resized image</p></div>
            </div>
        </section>
        <section class="section">
            <h2>More Free Tools</h2>
            <div class="grid"><a href="/social-media-image-dimensions/" class="card">All Image Dimensions<br><small style="color:var(--text-secondary)">2026 Guide</small></a><a href="/resize-image-for-printing/" class="card">Resize for Print<br><small style="color:var(--text-secondary)">300 DPI Ready</small></a><a href="/change-image-resolution/" class="card">Change Resolution<br><small style="color:var(--text-secondary)">DPI & PPI</small></a><a href="/image-size-guide/" class="card">Image Size Guide<br><small style="color:var(--text-secondary)">All Platforms</small></a><a href="/resize-jpg-online/" class="card">Resize JPG Online<br><small style="color:var(--text-secondary)">Format Specific</small></a><a href="/bulk-image-resizer/" class="card">Bulk Resizer<br><small style="color:var(--text-secondary)">Multiple Images</small></a></div>
        </section>
        <div class="cross-site">
            <strong>Pro Tip</strong> — Done resizing? Optimize file size with our <a href="https://compressnow.net">file optimizer</a>. Build a resume? <a href="https://cvbuild-ai.com">CVBuild-AI</a>. Write emails? <a href="https://messagegen-ai.com">MessageGen-AI</a>. Adjust tone? <a href="https://tonemodifier.com">ToneModifier</a>.
        </div>
        <section class="faq-section" id="faq">
            <div class="container">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-item"><h3>How does ResizeNow work?</h3><p>Upload your image, choose a platform preset or enter custom dimensions, and download the resized image. Everything happens in your browser — no upload to server.</p></div>
                <div class="faq-item"><h3>Is ResizeNow free?</h3><p>Yes, completely free. No signup, no watermarks, no limits. Resize as many images as you need.</p></div>
                <div class="faq-item"><h3>What platforms are supported?</h3><p>Instagram, TikTok, YouTube, Discord, LinkedIn, Facebook, X/Twitter, Pinterest, WhatsApp, Snapchat, and custom sizes.</p></div>
                <div class="faq-item"><h3>Is my image uploaded to a server?</h3><p>No. All processing happens locally in your browser. Your images never leave your device.</p></div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <p>&copy; 2026 ResizeNow. All rights reserved. | <a href="/">Home</a> | <a href="#faq">FAQ</a></p>
            <p style="margin-top:8px">All processing happens locally in your browser. Your images are never uploaded.</p>
        </div>
    </footer>
    <script>
    const PRESETS = {json.dumps(PRESETS)};
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const toolControls = document.getElementById('toolControls');
    const presetSelect = document.getElementById('presetSelect');
    const widthInput = document.getElementById('widthInput');
    const heightInput = document.getElementById('heightInput');
    const lockRatio = document.getElementById('lockRatio');
    const resizeBtn = document.getElementById('resizeBtn');
    const resetBtn = document.getElementById('resetBtn');
    const previewArea = document.getElementById('previewArea');
    const originalPreview = document.getElementById('originalPreview');
    const resizedPreview = document.getElementById('resizedPreview');
    const stats = document.getElementById('stats');
    const downloadPng = document.getElementById('downloadPng');
    const downloadJpg = document.getElementById('downloadJpg');

    let originalImage = null;
    let originalWidth = 0;
    let originalHeight = 0;
    let resizedCanvas = null;

    dropZone.addEventListener('click', () => fileInput.click());
    dropZone.addEventListener('dragover', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--primary)'; }});
    dropZone.addEventListener('dragleave', () => {{ dropZone.style.borderColor = 'var(--border)'; }});
    dropZone.addEventListener('drop', e => {{ e.preventDefault(); dropZone.style.borderColor = 'var(--border)'; if(e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]); }});
    fileInput.addEventListener('change', () => {{ if(fileInput.files.length) handleFile(fileInput.files[0]); }});
    presetSelect.addEventListener('change', () => {{ const p = PRESETS[presetSelect.value]; if(p) {{ widthInput.value = p.width; heightInput.value = p.height; }} }});
    widthInput.addEventListener('input', () => {{ if(lockRatio.checked && originalWidth) {{ heightInput.value = Math.round(widthInput.value * originalHeight / originalWidth); }} }});
    heightInput.addEventListener('input', () => {{ if(lockRatio.checked && originalHeight) {{ widthInput.value = Math.round(heightInput.value * originalWidth / originalHeight); }} }});
    resizeBtn.addEventListener('click', resizeImage);
    resetBtn.addEventListener('click', resetAll);
    downloadPng.addEventListener('click', () => download('png'));
    downloadJpg.addEventListener('click', () => download('jpeg'));

    function handleFile(file) {{ if(!file.type.match(/^image\\/(png|jpeg|webp)$/)) return; const reader = new FileReader(); reader.onload = e => {{ const img = new Image(); img.onload = () => {{ originalImage = img; originalWidth = img.width; originalHeight = img.height; originalPreview.src = e.target.result; widthInput.value = img.width; heightInput.value = img.height; dropZone.style.display = 'none'; toolControls.style.display = 'block'; }}; img.src = e.target.result; }}; reader.readAsDataURL(file); }}

    function resizeImage() {{ if(!originalImage) return; const w = parseInt(widthInput.value); const h = parseInt(heightInput.value); if(!w || !h) return; const canvas = document.createElement('canvas'); canvas.width = w; canvas.height = h; const ctx = canvas.getContext('2d'); ctx.drawImage(originalImage, 0, 0, w, h); resizedCanvas = canvas; resizedPreview.src = canvas.toDataURL(); const origSize = fileInput.files[0].size; const newSize = Math.round(canvas.toDataURL().length * 0.75); stats.innerHTML = '<div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px"><div><strong>Original:</strong> ' + originalWidth + ' x ' + originalHeight + '</div><div><strong>Resized:</strong> ' + w + ' x ' + h + '</div><div><strong>Original Size:</strong> ' + formatSize(origSize) + '</div><div><strong>New Size:</strong> ~' + formatSize(newSize) + '</div></div>'; previewArea.style.display = 'block'; }}

    function download(format) {{ if(!resizedCanvas) return; const link = document.createElement('a'); link.download = 'resized.' + (format === 'png' ? 'png' : 'jpg'); link.href = resizedCanvas.toDataURL('image/' + format, 0.92); link.click(); }}

    function resetAll() {{ originalImage = null; originalWidth = 0; originalHeight = 0; resizedCanvas = null; fileInput.value = ''; dropZone.style.display = 'block'; toolControls.style.display = 'none'; previewArea.style.display = 'none'; }}

    function formatSize(bytes) {{ if(bytes < 1024) return bytes + ' B'; if(bytes < 1048576) return (bytes/1024).toFixed(1) + ' KB'; return (bytes/1048576).toFixed(2) + ' MB'; }}
    </script>
</body>
</html>"""
    w("index.html", html)
    print("🏠 index.html")


def build_sitemap():
    urls = [f"https://{DOMAIN}/"]
    for s in ALL_SCENARIOS:
        urls.append(f"https://{DOMAIN}/{s['slug']}/")
    today = "2026-06-14"
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        p = "1.0" if u == f"https://{DOMAIN}/" else "0.8"
        xml += f"  <url><loc>{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n"
    xml += "</urlset>"
    w("sitemap.xml", xml)
    print(f"📄 sitemap.xml ({len(urls)} URLs)")


def build_robots():
    w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
    print("🤖 robots.txt")


def build_static():
    for slug, title, content in [
        ("privacy", "Privacy Policy", "<p>ResizeNow does not collect, store, or share any personal information. All image processing happens locally in your browser. Your images never leave your device.</p>"),
        ("terms", "Terms of Service", "<p>ResizeNow is provided as-is. Users are responsible for reviewing resized images before use. Excessive automated use is prohibited.</p>"),
        ("contact", "Contact Us", "<p>Email: contact@resizenow.net</p><p>We aim to respond within 2 business days.</p>"),
    ]:
        html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{title} | ResizeNow</title><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"><style>body{{font-family:'Inter',-apple-system,sans-serif;background:#FAFAFA;color:#1E293B;line-height:1.6}}.container{{max-width:720px;margin:0 auto;padding:0 24px}}header{{background:#1E293B;padding:16px 0}}header .container{{display:flex;align-items:center}}header a{{color:#F1F5F9;text-decoration:none;font-weight:700;font-size:1.2rem}}main{{padding:80px 0}}h1{{font-size:2rem;margin-bottom:24px}}p{{color:#64748B;margin-bottom:16px}}footer{{background:#1E293B;color:#94A3B8;padding:32px 0;text-align:center;font-size:.85rem}}footer a{{color:#CBD5E1;text-decoration:none}}</style></head><body><header><div class="container"><a href="/">ResizeNow</a></div></header><main><div class="container"><h1>{title}</h1>{content}</div></main><footer><div class="container"><p>&copy; 2026 ResizeNow. All rights reserved. | <a href="/">Home</a></p></div></footer></body></html>"""
        w(f"{slug}.html", html)
        print(f"  📋 {slug}.html")


def validate_scenarios(data, name="数据"):
    required = ['slug', 'title', 'desc']
    for i, s in enumerate(data):
        for f in required:
            if f not in s:
                raise KeyError(f"{name}[{i}] 缺字段 '{f}' — 标题: {s.get('title', 'N/A')}")
    print(f"✅ {name}校验通过: {len(data)} 条")

if __name__ == "__main__":
    validate_scenarios(ALL_SCENARIOS, "ALL_SCENARIOS")
    build_home()
    print(f"\n📄 {len(ALL_SCENARIOS)} Scenario Pages:")
    for s in ALL_SCENARIOS:
        w(f"{s['slug']}/index.html", build_scene_page(s))
        print(f"  📄 {s['slug']}/")
    build_sitemap()
    build_robots()
    build_static()
    print(f"\n✅ Build Complete — {1 + len(ALL_SCENARIOS) + 6} pages")
