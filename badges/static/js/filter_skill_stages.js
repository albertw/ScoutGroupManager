document.addEventListener('DOMContentLoaded', function() {

    const skillAreaSelect = document.querySelector('select[name="skill_area"]');
    const skillStageSelect = document.querySelector('select[name="skill_stage"]');

    skillAreaSelect.addEventListener('change', function() {
        const skillAreaId = skillAreaSelect.value;
        console.log('Selected Skill Area ID:', skillAreaId);  // Log selected value
        console.log('Selected Skill Area ID:', skillAreaSelect);  // Log selected value
        fetch(`/badges/get_skill_stages/${skillAreaId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                skillStageSelect.innerHTML = '';
                data.skill_stages.forEach(function(stage) {
                    const option = document.createElement('option');
                    option.value = stage.id;
                    option.textContent = stage.name + " " + stage.number;
                    skillStageSelect.appendChild(option);
                });
            });
    });
});