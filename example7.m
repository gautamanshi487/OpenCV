% Initialize video capture object
vid = videoinput('winvideo');

% Set video resolution (adjust as needed)
vid.VideoResolution = [320 240];

% Set number of frames to process (optional, 0 for continuous processing)
numFrames = 100;

% Create mouth detection cascade classifier
mouthDetector = vision.CascadeObjectDetector('Mouth');

while (numFrames == 0) || (vid.FramesAcquired < numFrames)

  % Get the next video frame
  frame = get(vid, 'LatestFrame');

  % Convert frame to grayscale for detection
  grayFrame = rgb2gray(frame);

  % Detect mouth in the frame
  mouth = step(mouthDetector, grayFrame);

  % Check if mouth is detected
  if ~isempty(mouth)
      % Mouth is open (detected)
      disp('Mouth is open');
  else
      % Mouth is closed (not detected)
      disp('Mouth is closed');
  end

  % Show the frame with bounding box (if mouth detected)
  if ~isempty(mouth)
      for i = 1:size(mouth, 1)
          rectangle('Position', mouth(i, :), 'LineWidth', 2, 'EdgeColor', 'red');
      end
  end
  imshow(frame);
end

% Release video capture object
release(vid);
