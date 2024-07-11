% Load the video capture device
vid = videoinput('winvideo', 1);

% Set up the face mesh detector
face_mesh = vision.FaceMeshDetector('MaxNumFaces', 1, 'MinDetectionConfidence', 0.5, 'MinTrackingConfidence', 0.5);

% Set up the mouth threshold
mouth_threshold = 0.004;

while true
    % Read a frame from the video capture devi2ce
    frame = getsnapshot(vid);
    
    % Convert the frame to RGB
    rgb_frame = frame(:, :, [3 2 1]);
    
    % Detect face landmarks
    [bboxes, scores, landmarks] = face_mesh(rgb_frame);
    
    % Check if a face was detected
    if ~isempty(landmarks)
        % Calculate the lip distance
        upper_lip_indices = [13, 14, 15, 16, 17];
        lower_lip_indices = [84, 85, 86, 87, 88];
        upper_lip_height = mean(landmarks(upper_lip_indices, 2));
        lower_lip_height = mean(landmarks(lower_lip_indices, 2));
        lip_distance = lower_lip_height - upper_lip_height;
        
        % Check if the mouth is open
        if lip_distance > mouth_threshold
            text = 'Opened';
        else
            text = 'Closed';
        end
        
        % Display the result
        imshow(rgb_frame);
        text(30, 30, text, 'Color', 'ed', 'FontSize', 18);
        drawnow;
    end
    
    % Check for keyboard input to exit
    if get(gcf, 'CurrentCharacter') == 27
        break
    end
end

% Release the video capture device
release(vid);