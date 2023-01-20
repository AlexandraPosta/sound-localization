classdef Environment
    %   Environment - Class used to define the properties of state space

    properties
        Name
        Sound
        Agent
        Accuracy
    end

    methods
        function obj = getSound()
            % obj.Sound =
            % call Sounds and generate a random sound
        end

        function obj = getAgent()
            % obj.Agent =
            % return the instance of the agent
        end

        function obj = getScore(estimation)
            % scoreX = estimation.X - obj.Sound.X
            % scoreY = estimation.Y - obj.Sound.Y
            % scoreZ = estimation.Z - obj.Sound.Z
            % compute accuracy based on the distance estimation for each coord
    end
end