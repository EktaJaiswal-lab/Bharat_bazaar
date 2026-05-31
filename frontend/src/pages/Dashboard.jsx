import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import { Activity, Users, DollarSign, TrendingUp } from 'lucide-react';
import axios from 'axios';

export default function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  const COLORS = ['#66fcf1', '#8a2be2', '#ff00ff', '#45a29e'];

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await axios.get('http://localhost:8000/analytics/dashboard');
        setData(res.data);
      } catch (err) {
        console.error("Error fetching analytics", err);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex justify-center items-center h-[60vh]">
        <div className="text-brand-cyan animate-pulse text-xl">Loading Analytics Core...</div>
      </div>
    );
  }

  if (!data) return null;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">Admin <span className="neon-text">Dashboard</span></h1>
        <Link to="/add-product" className="btn-primary flex items-center gap-2">
          <span className="text-xl leading-none">+</span> Add Product
        </Link>
      </div>
      
      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div className="glass p-6 rounded-xl flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm mb-1">Total Revenue</p>
            <h3 className="text-3xl font-bold text-white">{data.total_revenue}</h3>
          </div>
          <div className="p-3 bg-brand-purple/20 rounded-lg text-brand-purple">
            <DollarSign className="w-6 h-6" />
          </div>
        </div>
        
        <div className="glass p-6 rounded-xl flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm mb-1">Active Users</p>
            <h3 className="text-3xl font-bold text-white">{data.total_users}</h3>
          </div>
          <div className="p-3 bg-brand-cyan/20 rounded-lg text-brand-cyan">
            <Users className="w-6 h-6" />
          </div>
        </div>

        <div className="glass p-6 rounded-xl flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm mb-1">Conversion Rate</p>
            <h3 className="text-3xl font-bold text-white">{data.conversion_rate}</h3>
          </div>
          <div className="p-3 bg-brand-pink/20 rounded-lg text-brand-pink">
            <TrendingUp className="w-6 h-6" />
          </div>
        </div>

        <div className="glass p-6 rounded-xl flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm mb-1">System Status</p>
            <h3 className="text-xl font-bold text-green-400">Optimal</h3>
          </div>
          <div className="p-3 bg-green-500/20 rounded-lg text-green-400">
            <Activity className="w-6 h-6" />
          </div>
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Chart */}
        <div className="glass p-6 rounded-xl lg:col-span-2">
          <h3 className="text-lg font-semibold mb-6">Revenue vs Views (7 Days)</h3>
          <div className="h-[300px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={data.sales_trend} margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorSales" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#8a2be2" stopOpacity={0.8}/>
                    <stop offset="95%" stopColor="#8a2be2" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="colorViews" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#66fcf1" stopOpacity={0.8}/>
                    <stop offset="95%" stopColor="#66fcf1" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <XAxis dataKey="name" stroke="#cbd5e1" />
                <YAxis stroke="#cbd5e1" />
                <Tooltip contentStyle={{ backgroundColor: '#1f2833', borderColor: '#45a29e', color: '#fff' }} />
                <Area type="monotone" dataKey="sales" stroke="#8a2be2" fillOpacity={1} fill="url(#colorSales)" />
                <Area type="monotone" dataKey="views" stroke="#66fcf1" fillOpacity={1} fill="url(#colorViews)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Donut Chart */}
        <div className="glass p-6 rounded-xl lg:col-span-1">
          <h3 className="text-lg font-semibold mb-6">Sales by Category</h3>
          <div className="h-[300px] w-full flex justify-center items-center">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={data.category_distribution}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={100}
                  paddingAngle={5}
                  dataKey="value"
                  stroke="none"
                >
                  {data.category_distribution.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip contentStyle={{ backgroundColor: '#1f2833', borderColor: '#45a29e', color: '#fff' }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
