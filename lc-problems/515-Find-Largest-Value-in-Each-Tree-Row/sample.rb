#!/usr/bin/env ruby

class Solution
	def largest_values(root)
		return [] if root.nil?
		large(root).compact
	end

	def large(root)
		res=[]
		tmp = []
		compare = []
		queue=[root]
		while queue.size > 0
			node = queue.shift
			compare.push(node.val)
			tmp.push(node.left) if node.left
			tmp.push(node.right) if node.right
			if queue.size == 0
				res << compare.max
				queue = [] + tmp
				compare = []
				tmp = []
			end
		end
		res
	end
end