import cv2 as cv

#reading images
def read_images():
    img = cv.imread('photos/cat.jpg')
    # resized_image = rescaleFrame(img)
    cv.imshow('Cat', img)
    # cv.imshow('cat_r',resized_image)
    cv.waitKey(0)

#reading videos
def read_videos():
    capture = cv.VideoCapture('videos/dog.mp4') #0 for webcam
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video',frame)

        if cv.waitKey(20)  & 0xFF == ord('d'):
            break
    capture.release()

#rescale the frames of videos
def rescaleFrame(frame,scale=0.75):
    #this method will work for Images,Videos and Live Video

    width = int(frame.shape[1] * scale) #frame.shape[1] basically means the width of frame
    height = int(frame.shape[0] * scale) #frame.shape[0] basically means the height of frame
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #only work for live video
    capture.set(3,width)
    capture.set(4.height)


#after resizing yhe videos frame will play it on window
def read_resized_videos():
    capture = cv.VideoCapture('videos/dog.mp4') #0 for webcam
    while True:
        isTrue, frame = capture.read()
        resized_frame = rescaleFrame(frame)
        cv.imshow('Video',frame)
        cv.imshow('Video Resized',resized_frame)
        if cv.waitKey(20)  & 0xFF == ord('d'):
            break
    capture.release()


cv.destroyAllWindows()
