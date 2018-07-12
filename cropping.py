def cropping(image, filename):
    
    #Left Top Crop
    crop = image[:96, :96]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'leftTop' + '.png', crop)
    
    #Center Top Crop
    crop = image[:96, 16:112]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'centerTop' + '.png', crop)
    
    #Right Top Crop
    crop = image[:96, 32:]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'rightTop' + '.png', crop)
    
    #Left Center Crop
    crop = image[16:112, :96]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'leftCenter' + '.png', crop)
    
    #Center Center Crop
    crop = image[16:112, 16:112]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'centerCenter' + '.png', crop)
    
    #Right Center Crop
    crop = image[16:112, 32:]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'rightCenter' + '.png', crop)
    
    #Left Bottom Crop
    crop = image[32:, :96]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'leftBottom' + '.png', crop)
    
    #Center Bottom Crop
    crop = image[32:, 16:112]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'centerBottom' + '.png', crop)
    
    #Right Bottom Crop
    crop = image[32:, 32:]
    crop = cv2.resize(crop, (128, 128))
    cv2.imwrite(filename[:-4] + 'rightBottom' + '.png', crop)