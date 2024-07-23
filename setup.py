{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "010570b2-4b23-4d06-9eea-d67f196a26ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "from setuptools import setup, find_packages\n",
    "\n",
    "setup(\n",
    "    name=\"morsecode_aj\",\n",
    "    version=\"1.0.0\",\n",
    "    author=\"Akshaya Reddy\",\n",
    "    author_email=\"annareddyakshayar@gmail.com\",\n",
    "    description=\"A Morse Code Translator that converts between Morse code and English letters/numbers and produces a beep sound after translating.\",\n",
    "    long_description=open(\"README.md\").read(),\n",
    "    long_description_content_type=\"text/markdown\",\n",
    "    url=\"https://github.com/Akshaya-Reddi/Morsecode_aj\",\n",
    "    packages=find_packages(),\n",
    "    classifiers=[\n",
    "        \"Programming Language :: Python :: 3\",\n",
    "        \"License :: OSI Approved :: MIT License\",\n",
    "        \"Operating System :: OS Independent\",\n",
    "    ],\n",
    "    python_requires='>=3.6',\n",
    "    install_requires=[\n",
    "        # Add any other dependencies here\n",
    "    ],\n",
    "    entry_points={\n",
    "        'console_scripts': [\n",
    "            'morsecode_aj=MC:main',\n",
    "        ],\n",
    "    },\n",
    ")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
