import React from 'react';
import './App.css';
import 'antd/dist/antd.css';

import MainLayout from './containers/Layout'
import PetList from './containers/PetListView'

function App() {
	return (
		<div className="App">
			<MainLayout>
				<PetList/>
			</MainLayout>
		</div>
		);
	}
	
	export default App;
	