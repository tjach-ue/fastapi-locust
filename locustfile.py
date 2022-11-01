from locust import HttpUser, task
import random


class FactorialTest(HttpUser):
    test_samples = (1, 5, 10, 120, 237846)

    @task
    def endpoint1(self):
        self.client.get(f"/factor1/{random.choice(self.test_samples)}")

    @task
    def endpoint2(self):
        self.client.get(f"/factor2/{random.choice(self.test_samples)}")

    @task
    def endpoint3(self):
        self.client.get(f"/factor3/{random.choice(self.test_samples)}")