import React from "react"
import WordBox from "./WordBox.js"


class Forms extends React.Component{
	constructor(props){
		super(props)
		this.state = {
			prevLetters : "",
			letters : "",
			words : []
		}
		//Binds our function handles to this class
		this.updateInputtedField = this.updateInputtedField.bind(this)
		this.handleFormSubmission = this.handleFormSubmission.bind(this)
	}

	updateInputtedField(event){
		//Updates the state value with the current value of the search bar
        this.setState({ letters: event.target.value })
	}
	
	handleFormSubmission(event){
		//Updates our scrabble words using my custom scrabble api
		if(this.state.letters == ""){//Stops the api call from happening if we have nothing to pass it
			return;
		}
		//API call
		fetch("http://localhost:5000/scrabbleSolver/api/".concat(this.state.letters))
			.then(response => response.json())
            .then(response => {
                this.setState({ words: response })
            })
            .catch((error)=>{
				alert("Failed to contact scrabble API")
				throw new Error("Failed to contact scrabble API, Ensure CORS policy allows API calls")
			})
        //Update the letters in the search box along with the prevLetters used in the wordbox
        this.setState({prevLetters:this.state.letters})
        this.setState({letters:""})
		event.preventDefault()
	}

	

	render(){
		return(
			<div>
				
				<form class = "searchForm" onSubmit = {this.handleFormSubmission}>
					<label>
						<input 
						class = "form-control"
						type = "text" 
						placeholder = "Enter Letters"
						value = {this.state.letters}
						onChange = {this.updateInputtedField}
						/>
					</label>
					<input class="fa" type="submit" value="Submit" />
				</form>
				<WordBox wordList = {this.state.words} prevLetters = {this.state.prevLetters?this.state.prevLetters:""}/>
			</div>
		)
	}
} 


export default Forms