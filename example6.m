% Initialize video capture from the laptop camera
vid = videoinput('winvideo', 1, 'YUY2_640x480');
set(vid, 'ReturnedColorSpace', 'RGB');
triggerconfig(vid, 'manual');
vid.FramesPerTrigger = Inf;
vid.FrameGrabInterval = 5; % Capture every 5th frame

% Load the face detector
faceDetector = vision.CascadeObjectDetector();

% Start video acquisition
start(vid);
preview(vid);

% Create a figure window to display the video
hFig = figure;
hAxes = axes('Parent', hFig);

while ishandle(hFig)
    % Get the snapshot of the current frame
    frame = getsnapshot(vid);

    % Detect faces in the frame
    bbox = step(faceDetector, frame);

    if ~isempty(bbox)
        % For simplicity, assume the first detected face is the one we want
        faceBox = bbox(1, :);

        % Detect facial landmarks using the Python script
        landmarks = py.landmark_detection.detect_landmarks(frame);

        % Convert Python list to MATLAB array
        landmarks = cellfun(@double, cell(landmarks));

        % Plot the landmarks
        imshow(frame, 'Parent', hAxes);
        hold on;
        plot(landmarks(:,1), landmarks(:,2), 'g.', 'MarkerSize', 10);
        
        % Extract mouth landmarks (points 49 to 68 in the 68-point model)
        mouthLandmarks = landmarks(49:68, :);

        % Calculate the height of the mouth
        mouthHeight = mean(mouthLandmarks(9:12, 2)) - mean(mouthLandmarks(1:4, 2));
        
        % Threshold for mouth openness
        threshold = 10; % Adjust this threshold as needed

        if mouthHeight > threshold
            title(hAxes, 'Mouth is Open');
        else
            title(hAxes, 'Mouth is Closed');
        end

        hold off;
    else
        imshow(frame, 'Parent', hAxes);
        title(hAxes, 'No face detected');
    end

    % Allow MATLAB to process events
    drawnow;
end

% Clean up
stop(vid);
delete(vid);
