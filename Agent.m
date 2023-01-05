classdef Agent
    % Agent - Class used to define the agent that completes the sound localization

    properties
        PointingDirection
        X
        Y
        Z
        Mobility
        SoundData
        Model
        Score
    end

    methods
        function location = estSL(obj.SoundData, obj.Model)
        % estSL Estimates the location of the sound 
        % It relies on the algorithmic model selected for the agent 
            % return vector of (X, Y, Y)
        end

        % estimate the following coordinates based on score
    end
end