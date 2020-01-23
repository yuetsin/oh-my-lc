#!/usr/bin/env ruby

class Solution
    # @param {Integer[][]} grid
    # @return {Integer}
    def island_perimeter(grid)
        return 0 if grid.nil? || grid.size == 0
        perimeter = -Float::INFINITY
        visited = {}
        0.upto(grid.size-1) do|i|
            break if perimeter >= 0
            0.upto(grid[0].size-1) do |j|
                if grid[i][j] == 1
                    visited["#{i}-#{j}"] = true
                    perimeter = bfs(grid, i, j, visited)
                    break
                end
            end
        end
        perimeter
    end

    def bfs(grid, _r, _c, visited)
        count = 0
        rq = [_r]
        cq = [_c]
        while rq.size > 0
            r = rq.shift
            c = cq.shift
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while directions.size > 0
                direction = directions.shift
                rr = r + direction.first
                cc = c + direction.last
                if rr<0 || cc<0 || cc>=grid[0].size || rr>=grid.size || grid[rr][cc]==0
                    count += 1
                    next
                end
                if visited["#{rr}-#{cc}"].nil?
                    visited["#{rr}-#{cc}"] = true
                    rq << rr
                    cq << cc
                end
            end
        end
        count
    end
end
