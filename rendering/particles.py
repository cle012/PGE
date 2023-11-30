


class Particle:
    def __init__(self):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.density = density


class ParticleSystem:
    def __init__(self):
        # initialize the particle system
        self.particles = []


    def create_particles(self, position, velocity, color, density, count):
        # create particles with the same properties
        for _ in range(count):
            particle = Particle(position, velocity, color, density)
            self.particles.append(particle)

    def update_particles(self):
        #update particle positionand other properties
        for particle in self.particles:
            #update position based on velocity
            particle.position  +=  particle.velocity
            #add other logic to simulate particle behavioe (i.e., fading, scaling, etc)

