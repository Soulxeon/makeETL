import pandas as pd
import cv2

def dim(im):
    widthfix = int(im.shape[1] * 0.35)
    heightfix = int(im.shape[0] * 0.35)
    dim = (widthfix, heightfix)
    return dim

def visualDepthCheck(df):
    df['depths'] = df.apply(lambda x: openImage(x['filepath']),axis=1)
    df[['startdepth','enddepth','condition_error']] = pd.DataFrame(df['depths'].tolist(), index= df.index)
    df = df.drop(columns = 'depths')
    return(df)

def openImage(name):
    im = cv2.imread(name)
    im = cv2.resize(im, dim(im), interpolation=cv2.INTER_AREA)
    #resize
    cv2.imshow(name, im)
    while True:
        try:
            k = cv2.waitKey(10) & 0xFF
            if k != 27:
                sdepth = float(input('Start Depth:'))
                edepth = float(input('End Depth:'))
                break
            break
        except:
            print("not numeric value!")
    while True:
        k = cv2.waitKey(0)
        if k == ord('c'):
            error = 'Copy'
            break
        elif k == ord('x'):
            error = 'random'
            break
        elif k == ord('x'):
            error = 'No Core'
            break
        else:
            error = ''
            break

    cv2.destroyAllWindows()
    return([sdepth,edepth,error])
    


