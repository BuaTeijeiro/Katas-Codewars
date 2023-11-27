def count_smileys(arr):
    valid_faces = []
    valid_eyes = [':',';']
    valid_nose = ['','-','~']
    valid_mouth = [')','D']
    for eyes in valid_eyes:
        for nose in valid_nose:
            for mouth in valid_mouth:
                valid_faces.append(eyes + nose + mouth)
    
    valid_face_count = 0
    for face in arr:
        if face in valid_faces:
            valid_face_count += 1
        else:
            continue
    return valid_face_count