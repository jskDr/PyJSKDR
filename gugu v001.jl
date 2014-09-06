# It only shows the original multiplication table.
for x=2:9
	@printf("%d Level\n", x)
	for y=2:9
		z = x * y
		@printf( "%d x %d = %d \n", x, y, z)
	end
	println()
end

	
