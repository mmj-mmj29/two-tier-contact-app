# # Contact Manager - Flask + MySQL

A simple two-tier web application built using Python Flask and MySQL.

## Project Overview

This project demonstrates a basic two-tier architecture where:

- **Backend:** Python Flask web application
- **Database:** MySQL relational database

Users can add new contacts (name, email, phone) via a web form and view the list of saved contacts.

## Features

- Add contacts with name, email, and phone number
- View all saved contacts in a list
- Simple web interface using Flask's built-in templating

## Prerequisites

- Python 3.x
- MySQL server installed and running
- Python packages: `flask`, `mysql-connector-python`

## Setup Instructions

1. **Install dependencies**

```bash
sudo apt update
sudo apt install python3 python3-pip mysql-server
pip3 install flask mysql-connector-python
