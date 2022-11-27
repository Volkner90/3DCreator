translate([1.04,0.0,0.0]){
	rotate([90,0,90.0]){
		cube([0.35,0.4,1.14], center = true);
	}
}
difference() {
	difference() {
	translate([0.0,0,0.0]){
	rotate([0,90.0,0]){
		cube([1.5,1.5,2.0], center = true);
	}
}

	translate([-0.01,0,0.0]){
	rotate([90,0,0]){
		cylinder($fn = 12, h = 0.5, r1 = 0.26, r2 = 0.26, center = true);
	}
}
}

	translate([0.58,0,0.41]){
	rotate([0,90.0,0]){
		cube([0.3,0.3,0.4], center = true);
	}
}
}
difference() {
	difference() {
	translate([0,0.0,0.0]){
	rotate([0,90.0,90]){
		cube([2.25,2.25,3.0], center = true);
	}
}

	translate([0,0.0,0.02]){
	rotate([0,45.0,90]){
		cube([1.62,1.62,1.17], center = true);
	}
}
}

	translate([0,-0.1,-0.04]){
	rotate([0,90,0]){
		cylinder($fn = 3, h = 0.64, r1 = 0.42, r2 = 0.42, center = true);
	}
}
}
translate([0,1.88,-0.03]){
	rotate([0,90.0,90]){
		cube([1.41,1.41,0.75], center = true);
	}
}
