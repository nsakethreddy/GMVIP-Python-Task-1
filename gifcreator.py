Skip to content
Navigation Menu
nsakethreddy
/
LGMVIP

Type / to search
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Commit
Add files via upload
 main
@nsakethreddy
nsakethreddy committed 24 minutes ago 
1 parent f130061
commit c5fe1b6
Showing 1 changed file with 40 additions and 0 deletions.
 40 changes: 40 additions & 0 deletions40  
giffcreator.py
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,40 @@

from PIL import Image # type: ignore

def center_images_for_gif(image_paths, output_path, duration=500):
    images = [Image.open(img) for img in image_paths]

    # Find the maximum width and height among all images
    max_width = max(image.width for image in images)
    max_height = max(image.height for image in images)

    centered_images = []

    for img in images:
        # Create a new image with the maximum dimensions
        new_image = Image.new('RGBA', (max_width, max_height), (255, 255, 255, 0)) # Transparent background

        # Calculate position to paste the image centered
        paste_position = (
            (max_width - img.width) // 2,
            (max_height - img.height) // 2
        )

        # Paste the image onto the new image
        new_image.paste(img, paste_position)
        centered_images.append(new_image)

    # Save as GIF
    centered_images[0].save(
        output_path,
        save_all=True,
        append_images=centered_images[1:],
        duration=duration,
        loop=0,
        transparency=0
    )

# Example usage
image_files = ["image11.png", "image22.png", "image33.png"]
output_gif = "output_image.gif"
center_images_for_gif(image_files, output_gif)
0 comments on commit c5fe1b6
@nsakethreddy
Comment
 
Leave a comment
 
 You’re receiving notifications because you’re watching this repository.
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
Add files via upload · nsakethreddy/LGMVIP@c5fe1b6