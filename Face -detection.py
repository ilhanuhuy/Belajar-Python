{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "93d3e78a-6262-4f0c-a422-395a6d731cba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import PIL.Image\n",
    "import PIL.ImageDraw\n",
    "import face_recognition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a51b1b1a-744e-4b68-83d0-72e18fc1c0d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "given_image = face_recognition.load_image_file('kelas ML.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3d5ccae7-717f-4e01-ad26-870fbbfb4056",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We found 5 face(s) in this image.\n"
     ]
    }
   ],
   "source": [
    "face_locations = face_recognition.face_locations(given_image)\n",
    "\n",
    "number_of_faces = len(face_locations)\n",
    "print(\"We found {} face(s) in this image.\".format(number_of_faces))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e2b763be-2d00-4ad8-bba7-292361674465",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image = PIL.Image.fromarray(given_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7726ceb8-720d-4de5-8e19-07c86e2a2ae8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A face is detected at pixel location Top: 290, Left: 273, Bottom: 326, Right: 237\n",
      "A face is detected at pixel location Top: 190, Left: 85, Bottom: 226, Right: 49\n",
      "A face is detected at pixel location Top: 286, Left: 209, Bottom: 322, Right: 173\n",
      "A face is detected at pixel location Top: 202, Left: 797, Bottom: 238, Right: 761\n",
      "A face is detected at pixel location Top: 298, Left: 353, Bottom: 334, Right: 317\n"
     ]
    }
   ],
   "source": [
    "for face_location in face_locations:\n",
    "    top, left, bottom, right = face_location\n",
    "    print(\"A face is detected at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}\".format(top, left, bottom, right))\n",
    "    draw = PIL.ImageDraw.Draw(pil_image)\n",
    "    draw.rectangle([left, top, right, bottom], outline=\"green\", width=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6ac96c53-805a-469b-91ad-202792b4b137",
   "metadata": {},
   "outputs": [],
   "source": [
    "pil_image.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c63f909e-0a86-4205-9a9d-cec074a7794d",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
