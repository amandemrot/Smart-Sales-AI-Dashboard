export default function EconomicIndicatorsPage() {
    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-6">Economic Indicators</h1>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

                <div className="border rounded-xl p-6 shadow">
                    <h3 className="font-semibold text-lg">Inflation Rate</h3>
                    <p className="text-2xl mt-2 text-purple-600">6.2%</p>
                    <p className="text-sm text-gray-500 mt-1">Current CPI growth</p>
                </div>

                <div className="border rounded-xl p-6 shadow">
                    <h3 className="font-semibold text-lg">Fuel Price Index</h3>
                    <p className="text-2xl mt-2 text-purple-600">₹102.45</p>
                    <p className="text-sm text-gray-500 mt-1">Per litre</p>
                </div>

                <div className="border rounded-xl p-6 shadow">
                    <h3 className="font-semibold text-lg">Unemployment Rate</h3>
                    <p className="text-2xl mt-2 text-purple-600">7.8%</p>
                    <p className="text-sm text-gray-500 mt-1">National average</p>
                </div>

            </div>
        </div>
    )
}
