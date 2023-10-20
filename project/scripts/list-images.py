import os
from openstack import connection
from config.openstack_config import openstack_auth


def list_openstack_images():
    conn = connection.Connection(**openstack_auth)

    images = conn.image.images()
    print("List of available images:")
    for image in images:
        print(f"Image ID: {image.id}, Name: {image.name}")


if __name__ == "__main__":
    list_openstack_images()
