from cabin.models import *
from django.db.models import Q


def query_0(x):
    q = Driver.objects.filter(rating__gt=x)
    return q


def query_1(x):
    payment_sum = 0
    q = {}
    cars = Car.objects.filter(owner=x)
    for car in cars:
        rides = Ride.objects.filter(car=car)
        for ride in rides:
            payments = Payment.objects.filter(ride=ride)
            for payment in payments:
                payment_sum = payment_sum + payment.amount
    if payment_sum == 0:
        payment_sum = None

    q = {'payment_sum': payment_sum}
    return q


def query_2(x):
    q = []
    ride_request = RideRequest.objects.filter(rider=x)
    q = Ride.objects.filter(request__in=ride_request)

    return q


def query_3(t):
    q = 0
    rides = Ride.objects.all()
    for ride in rides:
        duration = ride.dropoff_time - ride.pickup_time
        if duration > t:
            q = q + 1
    return q


def query_4(x, y, r):
    drivers = Driver.objects.all()
    xs = []
    ys = []
    for driver in drivers:
        if (((x - driver.x) ** 2) + ((y - driver.y) ** 2)) <= (r ** 2):
            xs.append(driver.x)
            ys.append(driver.y)
    q = Driver.objects.filter(x__in=xs, y__in=ys, active=True)
    return q


def query_5(n, c):
    driver_list = []
    cars = Car.objects.filter(Q(car_type='A') | Q(color=c))
    drivers = Driver.objects.all()
    for driver in drivers:
        for car in cars:
            if car.owner.id == driver.id:
                driver_list.append(driver)

    for driver in driver_list:
        cars = Car.objects.filter(owner=driver)
        for car in cars:
            rides = Ride.objects.filter(car=car)
            if not rides.count() >= n:
                driver_list.remove(driver)
    driver_id_list = []
    for driver in driver_list:
        driver_id_list.append(driver.id)
    q = Driver.objects.filter(id__in=driver_id_list)
    return q


def query_6(x, t):
    payment_sum = 0
    selected_riders = []
    riders = Rider.objects.all()
    for rider in riders:
        ride_requests = RideRequest.objects.filter(rider=rider)
        rides = Ride.objects.filter(request__in=ride_requests)
        payments = Payment.objects.filter(ride__in=rides)
        for payment in payments:
            payment_sum = payment_sum + payment.amount
        if rides.count() >= x and payment_sum > t:
            selected_riders.append(rider)
    selected_riders_id = []
    for rider in selected_riders_id:
        selected_riders_id.append(rider.id)
    q = Rider.objects.filter(id__in=selected_riders_id)
    return q


def query_7():
    driver_list = []
    cars = Car.objects.all()
    drivers = Driver.objects.all()
    for driver in drivers:
        for car in cars:
            if car.owner.id == driver.id:
                driver_list.append(driver)

    for driver in driver_list:
        cars = Car.objects.filter(owner=driver)
        for car in cars:
            rides = Ride.objects.filter(car=car)
            if not rides.count() >= 1:
                driver_list.remove(driver)
    driver_id_list = []
    for driver in driver_list:
        driver_id_list.append(driver.id)

    driver_rides = []
    driver_result_list = []
    drivers_new = Driver.objects.filter(id__in=driver_id_list)
    for driver in drivers_new:
        cars = Car.objects.filter(owner=driver)
        for car in cars:
            rides1 = Ride.objects.filter(car=car)
            for ride1 in rides1:
                driver_rides.append(ride1.id)
                riders = Rider.objects.all()
                for rider in riders:
                    ride_requests = RideRequest.objects.filter(rider=rider)
                    for ride_request in ride_requests:
                        rides2 = Ride.objects.filter(request=ride_request)
                        for ride2 in rides2:
                            if ride2.id == ride1.id:
                                if rider.account.first_name in driver.account.first_name:
                                    driver_result_list.append(driver.id)
    driver_result_list = list(dict.fromkeys(driver_result_list))
    q = Driver.objects.filter(id__in=driver_result_list)
    return q


def query_8():
    q = 'your query here'
    return q


def query_9(n, t):
    q = 'your query here'
    return q


def query_10():
    q = 'your query here'
    return q
